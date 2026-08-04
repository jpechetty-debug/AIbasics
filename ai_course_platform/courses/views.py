"""
Views for the AI Course Platform.
"""
import json
import re
import markdown
from google import genai
from google.genai import types as genai_types
from google.genai import errors as genai_errors
from decouple import config
from pathlib import Path
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from django.utils import timezone
from django.db import models
from django.db.models import Count, Q, F, Value, IntegerField
from django.core.cache import cache
from .models import Module, Lesson, UserProgress, QuizAttempt, Certificate
from .utils import parse_quiz_content


_gemini_client = None

_PLACEHOLDER_API_KEYS = {'your-key-here', 'your_key_here', 'your_anthropic_api_key_here', 'your_gemini_api_key_here', 'changeme', ''}

GEMINI_MODEL = config('GEMINI_MODEL', default='gemini-3.6-flash')

def get_gemini_client():
    """Lazy-load and return a singleton Gemini client."""
    global _gemini_client
    if _gemini_client is None:
        api_key = config('GEMINI_API_KEY', default=None)
        if api_key:
            api_key = api_key.strip()
        if api_key and api_key.lower() not in _PLACEHOLDER_API_KEYS:
            _gemini_client = genai.Client(api_key=api_key)
    return _gemini_client

def throttle_public_ip(request, prefix='public_throttle_', limit=60):
    """Rate limiting based on IP address for public endpoints."""
    ip = request.META.get('REMOTE_ADDR')
    cache_key = f"{prefix}{ip}"
    request_count = cache.get(cache_key, 0)
    if request_count >= limit:
        return False
    cache.set(cache_key, request_count + 1, 3600)
    return True


def throttle_ai_tutor(user, prefix='ai_tutor_throttle_'):
    """Simple rate limiting using Django cache: 100 requests per hour (bypassed for staff)."""
    if getattr(user, 'is_staff', False) or getattr(user, 'is_superuser', False):
        return True
    cache_key = f"{prefix}{user.id}"
    request_count = cache.get(cache_key, 0)
    if request_count >= 100:
        return False
    # Set/update cache with incremented count, expiring in 1 hour
    cache.set(cache_key, request_count + 1, 3600)
    return True


class AITutorView(LoginRequiredMixin, View):
    """Handle chat queries for the AI Tutor using the real Gemini API."""
    def post(self, request, pk):
        try:
            data = json.loads(request.body)
            query = data.get('query', '')
            lesson = get_object_or_404(Lesson, pk=pk)
            
            # Load lesson content for context
            file_path = settings.CURRICULUM_DIR / lesson.file_path
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lesson_content = f.read()
            except Exception:
                lesson_content = "No content available for this lesson."

            if not throttle_ai_tutor(request.user, prefix='ai_tutor_throttle_'):
                return JsonResponse({
                    'success': False,
                    'error': 'Rate limit exceeded. You can send up to 100 messages per hour to the AI Tutor.'
                }, status=429)

            client = get_gemini_client()
            if not client:
                return JsonResponse({
                    'success': False, 
                    'error': 'AI Tutor is temporarily offline (API key not configured).'
                }, status=503)
            
            # Truncate content to avoid token limits
            context_text = lesson_content[:4000]
            
            system_prompt = f"""You are a helpful AI Tutor for the course "{lesson.module.title}".
Your goal is to help the student understand the following lesson: "{lesson.title}".

Context from the lesson material:
{context_text}

Instructions:
1. Be concise and professional.
2. If the student asks something outside the scope of this lesson, gently guide them back.
3. Use a helpful, encouraging tone.
4. If you don't know the answer based on the context, say so and suggest they review the lesson again.
"""

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=query,
                config=genai_types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    max_output_tokens=500,
                )
            )
            
            response_text = response.text
            
            return JsonResponse({
                'success': True,
                'response': response_text
            })
        except genai_errors.APIError:
            return JsonResponse({
                'success': False,
                'error': 'AI Tutor is temporarily offline (API key not configured).'
            }, status=503)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)


class PromptPlaygroundView(LoginRequiredMixin, View):
    """Interactive sandbox for testing prompts and logic patterns."""
    template_name = 'courses/prompt_playground.html'

    def get(self, request):
        """Render the playground with optional pre-filled prompt."""
        initial_prompt = request.GET.get('prompt', '')
        system_instructions = request.GET.get('system', 'You are a helpful AI assistant.')
        
        context = {
            'initial_prompt': initial_prompt,
            'system_instructions': system_instructions,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """Execute a prompt test."""
        try:
            data = json.loads(request.body)
            user_prompt = data.get('prompt', '')
            system_prompt = data.get('system', 'You are a helpful AI assistant.')
            
            # Input Validation (Hardening Issue 5)
            if len(system_prompt) > 2000:
                return JsonResponse({'success': False, 'error': 'System prompt too long (max 2,000 chars)'}, status=400)
            if len(user_prompt) > 5000:
                return JsonResponse({'success': False, 'error': 'User prompt too long (max 5,000 chars)'}, status=400)

            if not throttle_ai_tutor(request.user, prefix='playground_throttle_'):
                return JsonResponse({
                    'success': False,
                    'error': 'Rate limit exceeded. You can test up to 100 prompts per hour in the playground.'
                }, status=429)

            client = get_gemini_client()
            if not client:
                return JsonResponse({
                    'success': False, 
                    'error': 'AI Playground is temporarily offline (API key not configured).'
                }, status=503)

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=user_prompt,
                config=genai_types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    max_output_tokens=1000,
                )
            )
            
            return JsonResponse({
                'success': True,
                'response': response.text
            })
        except genai_errors.APIError:
            return JsonResponse({
                'success': False,
                'error': 'AI Playground is temporarily offline (API key not configured).'
            }, status=503)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)


class CertificateView(LoginRequiredMixin, View):
    """View and generate completion certificate."""
    template_name = 'courses/certificate.html'

    def get(self, request):
        # 1. Check if certificate already exists (Hardening Issue 4)
        certificate = Certificate.objects.filter(user=request.user).first()
        
        if certificate:
            return render(request, self.template_name, {'certificate': certificate})
        
        # 2. Check if eligible to issue new certificate
        total_lessons = Lesson.objects.count()
        completed_lessons = UserProgress.objects.filter(
            user=request.user,
            completed=True
        ).count()
        
        if total_lessons > 0 and completed_lessons >= total_lessons:
            # Atomic creation to avoid race conditions
            certificate, created = Certificate.objects.get_or_create(user=request.user)
            return render(request, self.template_name, {'certificate': certificate})
        
        return redirect('courses:dashboard')


class VerifyCertificateView(View):
    """Public view to verify certificate authenticity."""
    template_name = 'courses/certificate_verify.html'

    def get(self, request, uuid):
        if not throttle_public_ip(request, prefix='verify_cert_throttle_'):
            return render(request, self.template_name, {
                'error': 'Rate limit exceeded. Please try again in an hour.'
            }, status=429)
        
        certificate = get_object_or_404(Certificate, verification_uuid=uuid)
        return render(request, self.template_name, {'certificate': certificate})


class CourseMixin:
    """Shared logic for curriculum data."""
    def get_grouped_modules(self, user=None):
        # Base queryset with lesson count
        queryset = Module.objects.annotate(
            total_lessons_count=Count('lessons', distinct=True)
        )
        
        # Add completion count if user is authenticated
        if user and user.is_authenticated:
            queryset = queryset.annotate(
                completed_lessons_count=Count(
                    'lessons__user_progress',
                    filter=Q(
                        lessons__user_progress__user=user,
                        lessons__user_progress__completed=True
                    ),
                    distinct=True
                )
            )
        else:
            queryset = queryset.annotate(completed_lessons_count=Value(0, output_field=IntegerField()))

        modules = queryset.prefetch_related('lessons').all().order_by('order')
        phases_dict = {}
        
        for module in modules:
            total = module.total_lessons_count
            completed = getattr(module, 'completed_lessons_count', 0)
            progress = int((completed / total) * 100) if total > 0 else 0
            
            module_data = {
                'module': module,
                'progress': progress,
                'completed': completed,
                'total': total,
            }

            phase_key = module.phase_id or 'other'
            if phase_key not in phases_dict:
                phases_dict[phase_key] = {
                    'title': module.phase_title or 'Continuing Education',
                    'id': phase_key,
                    'modules': []
                }
            phases_dict[phase_key]['modules'].append(module_data)
        
        return sorted(phases_dict.values(), key=lambda x: x['modules'][0]['module'].order if x['modules'] else 999)


class DashboardView(CourseMixin, View):
    """Course dashboard with progress overview."""
    template_name = 'courses/dashboard.html'

    def get(self, request):
        phases = self.get_grouped_modules(request.user)
        
        # Calculate overall stats
        total_lessons = Lesson.objects.count()
        completed_lessons = 0
        if request.user.is_authenticated:
            completed_lessons = UserProgress.objects.filter(
                user=request.user,
                completed=True
            ).count()
        
        overall_progress = int((completed_lessons / total_lessons) * 100) if total_lessons > 0 else 0
        
        context = {
            'phases': phases,
            'overall_progress': overall_progress,
            'total_lessons': total_lessons,
            'completed_lessons': completed_lessons,
        }
        return render(request, self.template_name, context)


class ModuleDetailView(LoginRequiredMixin, DetailView, CourseMixin):
    """Module detail showing all lessons."""
    model = Module
    template_name = 'courses/module_detail.html'
    context_object_name = 'module'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        module = self.object
        lessons = module.lessons.all()
        
        # Performance optimization: pre-fetch all completed lesson IDs for this module at once
        completed_ids = set()
        if self.request.user.is_authenticated:
            completed_ids = set(UserProgress.objects.filter(
                user=self.request.user,
                lesson__module=module,
                completed=True
            ).values_list('lesson_id', flat=True))

        lessons_with_status = [
            {
                'lesson': l,
                'is_completed': l.pk in completed_ids
            } for l in lessons
        ]
        
        context['lessons_with_status'] = lessons_with_status
        context['phases'] = self.get_grouped_modules(self.request.user)
        
        # Calculate module progress using cached IDs
        total_lessons = lessons.count()
        completed_lessons = len(completed_ids)
        
        progress = int((completed_lessons / total_lessons) * 100) if total_lessons > 0 else 0
        context['progress'] = progress
        context['progress_offset'] = int(251.2 * (1 - progress / 100))
        
        return context


class QuizParsingMixin:
    """Mixin to provide shared quiz parsing logic for both lessons and assessments."""
    
    QUIZ_MARKERS = ["## Interactive Daily Quiz", "## 📝 Daily Quiz", "## Knowledge Check", "## Quiz"]

    def parse_quiz_content(self, content):
        """Robustly parse questions, options, feedback, and metadata from markdown content."""
        return parse_quiz_content(content)

    def sanitize_quiz_data(self, quiz_data):
        """Remove correct answers and feedback before sending to template context."""
        if not quiz_data:
            return quiz_data
        
        sanitized = []
        for q in quiz_data:
            safe_q = {
                'number': q.get('number'),
                'text': q.get('text'),
                'options': q.get('options'),
                'type': q.get('type')
            }
            sanitized.append(safe_q)
        return sanitized



class LessonDetailView(LoginRequiredMixin, DetailView, QuizParsingMixin, CourseMixin):
    """Lesson detail with markdown rendering."""
    model = Lesson
    template_name = 'courses/lesson_detail.html'
    context_object_name = 'lesson'

    def get_queryset(self):
        return super().get_queryset().select_related('module')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson = self.object
        
        file_path = settings.CURRICULUM_DIR / lesson.file_path
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                raw_content = f.read()
        except FileNotFoundError:
            raw_content = "# Content not found\n\nThe requested lesson file could not be found."
        except Exception as e:
            raw_content = f"# Error\n\nThere was an error loading the content: {e}"

        # 1. Consolidated Performance: HTML Rendering with Cache
        cache_key = f"lesson_html_{lesson.id}_{int(lesson.updated_at.timestamp())}"
        content_html = cache.get(cache_key)
        if not content_html:
            content_html = self.render_lesson_content(raw_content)
            cache.set(cache_key, content_html, 3600) # 1 hour cache
        
        context['content_html'] = content_html
        
        # 2. Consolidated Performance: Parse daily quiz from the same raw_content
        daily_quiz = self.parse_daily_quiz(raw_content)
        context['daily_quiz'] = daily_quiz
        
        # Strip answers before serializing to JSON for the template
        safe_daily_quiz = self.sanitize_quiz_data(daily_quiz)
        context['daily_quiz_json'] = json.dumps(safe_daily_quiz) if safe_daily_quiz else 'null'
        
        # Metadata and Navigation
        context['module_title'] = lesson.module.title
        context['module_slug'] = lesson.module.slug
        context['prev_lesson'] = lesson.get_previous_lesson()
        context['next_lesson'] = lesson.get_next_lesson()
        context['phases'] = self.get_grouped_modules(self.request.user)
        
        # Completion status
        if self.request.user.is_authenticated:
            context['is_completed'] = UserProgress.objects.filter(
                user=self.request.user,
                lesson=lesson,
                completed=True
            ).exists()
        else:
            context['is_completed'] = False
        
        return context

    def render_lesson_content(self, content):
        """Render markdown content, excluding daily quiz if it exists."""
        try:
            # Remove frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    content = parts[2]
            
            # If there's a daily quiz, hide it from main content to avoid duplication
            for marker in self.QUIZ_MARKERS:
                if marker in content:
                    content = content.split(marker)[0]
                    break
            
            # Remove the first H1 header from the markdown to prevent duplication
            content = re.sub(r'^#\s+.+?(\r?\n|$)', '', content.strip(), count=1)
            
            # Support for [!AI] callouts: > [!AI] message
            def replace_ai_callout(match):
                block = match.group(0)
                if '[!AI]' in block:
                    # Strip leading '>' and '[!AI]'
                    lines = [re.sub(r'^>\s*', '', line) for line in block.split('\n')]
                    content_lines = [re.sub(r'^\[!AI\]\s*', '', line, flags=re.IGNORECASE) for line in lines]
                    inner_html = '\n'.join(content_lines).strip()
                    return f'<div class="ai-insight">\n{inner_html}\n</div>'
                return block

            # Match consecutive blockquote lines
            content = re.split(r'(\n\n)', content)
            content = [re.sub(r'(^>.*(?:\n>.*)*)', replace_ai_callout, part, flags=re.MULTILINE) for part in content]
            content = ''.join(content)
            
            # Convert markdown to HTML
            md = markdown.Markdown(extensions=[
                'tables',
                'fenced_code',
                'codehilite',
                'toc',
                'nl2br',
            ])
            return md.convert(content)
        except Exception as e:
            return f'<p class="text-red-500">Error rendering content: {e}</p>'

    def parse_daily_quiz(self, content):
        """Detect and parse daily quiz section from content string."""
        try:
            # Look for quiz sections
            quiz_content = ""
            for marker in self.QUIZ_MARKERS:
                if marker in content:
                    quiz_content = content.split(marker)[1]
                    break
            
            if not quiz_content:
                return None
            
            return self.parse_quiz_content(quiz_content)
        except Exception as e:
            import logging
            logging.warning(f"Error parsing daily quiz: {e}")
            return None


class AssessmentView(LoginRequiredMixin, DetailView, QuizParsingMixin, CourseMixin):
    """Assessment/quiz view with interactive questions."""
    model = Lesson
    template_name = 'courses/assessment.html'
    context_object_name = 'lesson'

    def get_queryset(self):
        return Lesson.objects.filter(content_type='assessment')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson = self.object
        
        # Parse quiz questions from markdown
        file_path = settings.CURRICULUM_DIR / lesson.file_path
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            questions = self.parse_quiz_content(content)
        except Exception:
            questions = []
            
        # Flattened context for reliable template rendering
        context['module_title'] = lesson.module.title
        context['module_slug'] = lesson.module.slug
            
        context['questions'] = questions
        
        # Strip answers before serializing to JSON for the template
        safe_questions = self.sanitize_quiz_data(questions)
        context['questions_json'] = json.dumps(safe_questions)
        
        # Grouped modules for sidebar
        context['phases'] = self.get_grouped_modules(self.request.user)
        
        # Previous attempts
        if self.request.user.is_authenticated:
            context['previous_attempts'] = QuizAttempt.objects.filter(
                user=self.request.user,
                lesson=lesson
            )[:5]
        
        return context


@login_required
@require_POST
@csrf_protect
def mark_lesson_complete(request, pk):
    """Mark a lesson as complete via AJAX."""
    lesson = get_object_or_404(Lesson, pk=pk)
    
    progress, created = UserProgress.objects.get_or_create(
        user=request.user,
        lesson=lesson,
    )
    
    if not progress.completed:
        progress.completed = True
        progress.completed_at = timezone.now()
        progress.save()
    
    return JsonResponse({
        'success': True,
        'completed': True,
        'message': 'Lesson marked as complete!'
    })


@login_required
@require_POST
@csrf_protect
def submit_quiz(request, pk):
    """Submit quiz answers and calculate score."""
    lesson = get_object_or_404(Lesson, pk=pk)
    
    try:
        data = json.loads(request.body)
        answers = data.get('answers', {})
        # SECURITY FIX: Do NOT trust questions sent from client.
        # Load them from the server-side instead.
        file_path = settings.CURRICULUM_DIR / lesson.file_path
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # If it's a daily lesson, we need to extract the quiz section first
        if lesson.content_type == 'lesson':
            quiz_content = ""
            for marker in QuizParsingMixin.QUIZ_MARKERS:
                if marker in content:
                    quiz_content = content.split(marker)[1]
                    break
            questions = parse_quiz_content(quiz_content) if quiz_content else []
        else:
            questions = parse_quiz_content(content)
            
    except (json.JSONDecodeError, FileNotFoundError, Exception) as e:
        return JsonResponse({'error': f'Error processing quiz: {str(e)}'}, status=400)
    
    # Calculate score
    score = 0
    total = len(questions)
    results = []
    
    for q in questions:
        q_num = str(q['number'])
        user_answer = answers.get(q_num, [])
        if isinstance(user_answer, str):
            user_answer = [user_answer]
        
        correct = sorted(q['correct'])
        user_sorted = sorted(user_answer)
        is_correct = correct == user_sorted
        
        if is_correct:
            score += 1
        
        results.append({
            'number': q['number'],
            'correct': is_correct,
            'correct_answer': q['correct'],
            'user_answer': user_answer,
        })
    
    percentage = round((score / total) * 100, 2) if total > 0 else 0
    
    # Save attempt
    QuizAttempt.objects.create(
        user=request.user,
        lesson=lesson,
        score=score,
        total_questions=total,
        percentage=percentage,
        answers=answers,
    )
    
    # Mark lesson as complete if passed
    if percentage >= 70:
        progress, _ = UserProgress.objects.get_or_create(
            user=request.user,
            lesson=lesson,
        )
        if not progress.completed:
            progress.completed = True
            progress.completed_at = timezone.now()
            progress.save()
    
    return JsonResponse({
        'success': True,
        'score': score,
        'total': total,
        'percentage': percentage,
        'results': results,
        'passed': percentage >= 70,
    })

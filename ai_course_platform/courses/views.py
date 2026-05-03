"""
Views for the AI Course Platform.
"""
import json
import re
import markdown
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
from .models import Module, Lesson, UserProgress, QuizAttempt


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


class ModuleDetailView(DetailView, CourseMixin):
    """Module detail showing all lessons."""
    model = Module
    template_name = 'courses/module_detail.html'
    context_object_name = 'module'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        module = self.object
        lessons = module.lessons.all()
        
        # Add completion status for each lesson
        lessons_with_status = []
        for lesson in lessons:
            is_completed = False
            if self.request.user.is_authenticated:
                is_completed = UserProgress.objects.filter(
                    user=self.request.user,
                    lesson=lesson,
                    completed=True
                ).exists()
            lessons_with_status.append({
                'lesson': lesson,
                'is_completed': is_completed,
            })
        
        context['lessons_with_status'] = lessons_with_status
        context['phases'] = self.get_grouped_modules(self.request.user)
        
        # Calculate module progress
        total_lessons = lessons.count()
        completed_lessons = 0
        if self.request.user.is_authenticated:
            completed_lessons = UserProgress.objects.filter(
                user=self.request.user,
                lesson__module=module,
                completed=True
            ).count()
        
        progress = int((completed_lessons / total_lessons) * 100) if total_lessons > 0 else 0
        context['progress'] = progress
        context['progress_offset'] = int(251.2 * (1 - progress / 100))
        
        return context


class QuizParsingMixin:
    """Mixin to provide shared quiz parsing logic for both lessons and assessments."""
    
    def parse_quiz_content(self, content):
        """Robustly parse questions, options, feedback, and metadata from markdown content."""
        questions = []
        
        # Remove frontmatter if present
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2]
        
        # Use ### Question N or **Q N: as question markers
        # We split by the pattern to get individual blocks
        question_blocks = re.split(r'### Question \s*\d+|\*\*Q\d+:', content)[1:]
        
        for i, block in enumerate(question_blocks, start=1):
            # Extract question text (usually between **stars** or just the first line)
            q_text_match = re.search(r'\*\*(.+?)\*\*', block)
            if q_text_match:
                q_text = q_text_match.group(1).strip()
            else:
                # Fallback to first non-empty line
                lines = [l.strip() for l in block.split('\n') if l.strip()]
                q_text = lines[0] if lines else f"Question {i}"
            
            # Extract options
            options = []
            # Ensure the option start (e.g. "A)") is at the beginning of a line to avoid
            # matching acronyms in parentheses like "(UEBA)"
            option_matches = re.findall(r'^\s*([A-E])\)\s*(.+?)(?=\n\s*[A-E]\)|$|(?:\n\s*\*\*))', block, re.MULTILINE | re.DOTALL)
            for opt_letter, opt_text in option_matches:
                options.append({
                    'letter': opt_letter.strip(),
                    'text': opt_text.strip().replace('\n', ' ').strip().replace('**', '')
                })
            
            # Extract correct answer
            correct_match = re.search(r'\*\*Correct Answer(?:s?):\*\*\s*([A-E, \s]+)', block, re.IGNORECASE)
            if not correct_match:
                # Fallback search without stars
                correct_match = re.search(r'Correct Answer:\s*([A-E, \s]+)', block, re.IGNORECASE)
            
            if not correct_match: continue
            correct = [c.strip() for c in correct_match.group(1).split(',')]
            
            # Extract feedback
            feedback_match = re.search(r'\*\*Feedback:\*\*\s*\n(.*?)(?=\n\s*---|\n\s*\*\*Why|$)', block, re.DOTALL)
            if not feedback_match:
                feedback_match = re.search(r'Feedback:\s*\n(.*?)(?=\n\s*---|\n\s*\*\*Why|$)', block, re.DOTALL)
            
            feedback = feedback_match.group(1).strip() if feedback_match else ""
            
            # Extract "Why this matters"
            why_match = re.search(r'\*\*Why this matters.*?\*\*\s*:?\s*(.*?)(?=\n\s*---|$)', block, re.DOTALL | re.IGNORECASE)
            why_matters = why_match.group(1).strip() if why_match else ""
            
            q_type = 'multiple' if len(correct) > 1 else 'single'
            
            questions.append({
                'number': i,
                'text': q_text,
                'options': options,
                'correct': correct,
                'type': q_type,
                'feedback': feedback,
                'why_matters': why_matters
            })
            
        return questions


class LessonDetailView(DetailView, QuizParsingMixin, CourseMixin):
    """Lesson detail with markdown rendering."""
    model = Lesson
    template_name = 'courses/lesson_detail.html'
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson = self.object
        
        # Normalize path for Linux compatibility
        normalized_path = lesson.file_path.replace('\\', '/')
        file_path = settings.CURRICULUM_DIR / normalized_path
        
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
        context['daily_quiz_json'] = json.dumps(daily_quiz) if daily_quiz else 'null'
        
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
            quiz_markers = ["## Interactive Daily Quiz", "## 📝 Daily Quiz", "## Knowledge Check", "## Quiz"]
            for marker in quiz_markers:
                if marker in content:
                    content = content.split(marker)[0]
                    break
            
            # Remove the first H1 header from the markdown to prevent duplication
            content = re.sub(r'^#\s+.+?(\r?\n|$)', '', content.strip(), count=1)
            
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
            quiz_markers = ["## Interactive Daily Quiz", "## 📝 Daily Quiz", "## Knowledge Check", "## Quiz"]
            quiz_content = ""
            for marker in quiz_markers:
                if marker in content:
                    quiz_content = content.split(marker)[1]
                    break
            
            if not quiz_content:
                return None
            
            return self.parse_quiz_content(quiz_content)
        except Exception as e:
            print(f"Error parsing daily quiz: {e}")
            return None


class AssessmentView(DetailView, QuizParsingMixin, CourseMixin):
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
        # Normalize path for Linux compatibility
        normalized_path = lesson.file_path.replace('\\', '/')
        file_path = settings.CURRICULUM_DIR / normalized_path
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
        context['questions_json'] = json.dumps(questions)
        
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
        questions = data.get('questions', [])
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid data'}, status=400)
    
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

"""
Django models for the AI Course Platform.
"""
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Module(models.Model):
    """Represents a week/module in the curriculum."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    folder_name = models.CharField(max_length=100)  # e.g., 'week1'
    phase_title = models.CharField(max_length=200, blank=True)
    phase_id = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    def __str__(self):
        return f"Week {self.order}: {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_completion_percentage(self, user):
        """Calculate completion percentage for a user."""
        if not user.is_authenticated:
            return 0
        total_lessons = self.lessons.count()
        if total_lessons == 0:
            return 0
        completed = UserProgress.objects.filter(
            user=user,
            lesson__module=self,
            completed=True
        ).count()
        return int((completed / total_lessons) * 100)


class Lesson(models.Model):
    """Represents a single lesson/day in a module."""
    CONTENT_TYPE_CHOICES = [
        ('lesson', 'Lesson'),
        ('assessment', 'Assessment'),
    ]

    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    file_path = models.CharField(max_length=500)  # Relative path to the markdown file
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES, default='lesson')
    difficulty = models.CharField(max_length=50, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    replit_url = models.URLField(max_length=500, blank=True, null=True, help_text="Link to a Replit coding environment")
    codespaces_url = models.URLField(max_length=500, blank=True, null=True, help_text="Link to a GitHub Codespaces environment")
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['module__order', 'order']
        unique_together = ['module', 'slug']
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return f"{self.module.folder_name} - {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_next_lesson(self):
        """Get the next lesson in order."""
        # First try within same module
        next_in_module = Lesson.objects.filter(
            module=self.module,
            order__gt=self.order
        ).first()
        if next_in_module:
            return next_in_module
        
        # Try first lesson of next module
        next_module = Module.objects.filter(order__gt=self.module.order).first()
        if next_module:
            return next_module.lessons.first()
        return None

    def get_previous_lesson(self):
        """Get the previous lesson in order."""
        # First try within same module
        prev_in_module = Lesson.objects.filter(
            module=self.module,
            order__lt=self.order
        ).order_by('-order').first()
        if prev_in_module:
            return prev_in_module
        
        # Try last lesson of previous module
        prev_module = Module.objects.filter(order__lt=self.module.order).order_by('-order').first()
        if prev_module:
            return prev_module.lessons.order_by('-order').first()
        return None


class UserProgress(models.Model):
    """Tracks user progress on lessons."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='user_progress')
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'lesson']
        verbose_name = 'User Progress'
        verbose_name_plural = 'User Progress'

    def __str__(self):
        status = '✓' if self.completed else '○'
        return f"{self.user.username} - {self.lesson.title} [{status}]"


class QuizAttempt(models.Model):
    """Records quiz/assessment attempts."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_attempts')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='quiz_attempts')
    score = models.PositiveIntegerField(default=0)
    total_questions = models.PositiveIntegerField(default=0)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    answers = models.JSONField(default=dict)  # Store user answers
    attempted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-attempted_at']
        verbose_name = 'Quiz Attempt'
        verbose_name_plural = 'Quiz Attempts'

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}: {self.percentage}%"


class Certificate(models.Model):
    """Permanent record of course completion."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='certificate')
    issued_at = models.DateTimeField(auto_now_add=True)
    verification_uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    
    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    def __str__(self):
        return f"Certificate for {self.user.username} (Issued: {self.issued_at.date()})"




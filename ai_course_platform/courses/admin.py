from django.contrib import admin
from .models import Module, Lesson, UserProgress, QuizAttempt, Certificate


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'folder_name', 'created_at']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['order']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'module', 'content_type', 'order', 'created_at']
    list_filter = ['module', 'content_type']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['module__order', 'order']


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'completed', 'completed_at']
    list_filter = ['completed', 'lesson__module']
    search_fields = ['user__username', 'lesson__title']


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'score', 'total_questions', 'percentage', 'attempted_at']
    list_filter = ['lesson__module']
    search_fields = ['user__username']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['user', 'issued_at', 'verification_uuid']
    list_filter = ['issued_at']
    search_fields = ['user__username', 'user__email', 'verification_uuid']
    readonly_fields = ['verification_uuid', 'issued_at']

"""
URL patterns for the courses app.
"""
from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    # Dashboard
    path('', views.DashboardView.as_view(), name='dashboard'),
    
    # Module views
    path('module/<slug:slug>/', views.ModuleDetailView.as_view(), name='module_detail'),
    
    # Lesson views
    path('lesson/<int:pk>/', views.LessonDetailView.as_view(), name='lesson_detail'),
    
    # Assessment views
    path('assessment/<int:pk>/', views.AssessmentView.as_view(), name='assessment'),
    
    # API endpoints
    path('api/lesson/<int:pk>/complete/', views.mark_lesson_complete, name='mark_complete'),
    path('api/quiz/<int:pk>/submit/', views.submit_quiz, name='submit_quiz'),
]

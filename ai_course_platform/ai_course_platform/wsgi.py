"""
WSGI config for AI Course Platform.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_course_platform.settings')
application = get_wsgi_application()

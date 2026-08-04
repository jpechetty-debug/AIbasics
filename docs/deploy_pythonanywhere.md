# Deploying AI Basics Platform to PythonAnywhere

This guide provides step-by-step instructions for deploying the Django-based AI Basics course platform on PythonAnywhere.

## 1. Web App Setup
1. Log into your **PythonAnywhere** account.
2. Navigate to the **Web** tab and click **Add a new web app**.
3. Choose **Manual configuration** and select **Python 3.10+**.

## 2. Code & Virtual Environment Setup
In the PythonAnywhere Bash console:
```bash
git clone https://github.com/jpechetty-debug/AIbasics.git
cd AIbasics
python -m venv .venv
source .venv/bin/activate
pip install -r ai_course_platform/requirements.txt
```

## 3. Environment Variables (.env)
Create `ai_course_platform/.env`:
```ini
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com
GEMINI_API_KEY=your-gemini-api-key
GEMINI_MODEL=gemini-2.5-flash
```

## 4. Database & Static Files
```bash
cd ai_course_platform
python manage.py migrate
python manage.py load_curriculum
python manage.py collectstatic --noinput
```

## 5. WSGI Configuration
In your PythonAnywhere WSGI configuration file (`/var/www/yourusername_pythonanywhere_com_wsgi.py`):
```python
import os
import sys

path = '/home/yourusername/AIbasics/ai_course_platform'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ai_course_platform.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## 6. Reload Web App
Click **Reload yourusername.pythonanywhere.com** in the PythonAnywhere dashboard.

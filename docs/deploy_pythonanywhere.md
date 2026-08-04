# Deploying AI Basics Platform to PythonAnywhere

This guide provides step-by-step instructions for deploying the Django-based AI Basics course platform on [PythonAnywhere](https://www.pythonanywhere.com/).

## 1. Prerequisites
- A PythonAnywhere account (a free "Beginner" account works for SQLite, but note free accounts have restricted outbound internet access which might block API calls if not allowlisted. The Gemini API endpoint may require a paid PythonAnywhere account if it's not on their whitelist).
- A Gemini API Key for the AI Tutor (https://aistudio.google.com/app/apikey).
- Your code pushed to a GitHub repository.

## 2. Setting Up Your Environment
1. Log in to your PythonAnywhere account.
2. Go to the **Consoles** tab and start a new **Bash** console.
3. Clone your GitHub repository:
   ```bash
   git clone https://github.com/your-username/Ai-basicscourse.git
   ```
4. Create a virtual environment (replace `3.10` with the Python version you want to use):
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 ai-course-venv
   ```
5. Navigate into your project and install the requirements:
   ```bash
   cd Ai-basicscourse/ai_course_platform
   pip install -r requirements.txt
   ```

## 3. Environment Variables
1. While still in the `ai_course_platform` folder, create your `.env` file:
   ```bash
   cp .env.example .env
   nano .env
   ```
2. Update the values in `.env`:
   - `SECRET_KEY`: Enter a strong, random string.
   - `DEBUG`: Set to `False`.
   - `ALLOWED_HOSTS`: Set to `yourusername.pythonanywhere.com` (replace `yourusername` with your actual PythonAnywhere username).
   - `CSRF_TRUSTED_ORIGINS`: Set to `https://yourusername.pythonanywhere.com`.
   - `GEMINI_API_KEY`: Add your Google Gemini API key.
   - `GEMINI_MODEL`: e.g., `gemini-3.6-flash`.
3. Save and exit (in nano, press `Ctrl+O`, `Enter`, then `Ctrl+X`).

## 4. Run Migrations & Collect Static Files
In the same Bash console, run:
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

## 5. Web Tab Configuration
1. Go to the **Web** tab in PythonAnywhere and click **Add a new web app**.
2. Select your domain name (e.g., `yourusername.pythonanywhere.com`).
3. Select **Manual configuration** (not the Django one) and choose **Python 3.10** (or your chosen version).
4. **Virtualenv**: In the "Virtualenv" section, enter the name of your virtualenv: `ai-course-venv` (or the full path `/home/yourusername/.virtualenvs/ai-course-venv`).
5. **Source code**: In the "Code" section, set the "Source code" path to `/home/yourusername/Ai-basicscourse/ai_course_platform`.
6. **Working directory**: Set this to `/home/yourusername/Ai-basicscourse/ai_course_platform`.

## 6. Configure the WSGI File
1. In the **Code** section of the Web tab, click on the link for the **WSGI configuration file** (it looks like `/var/www/yourusername_pythonanywhere_com_wsgi.py`).
2. Delete the entire contents of the file and replace it with the following:

```python
import os
import sys
from pathlib import Path
from decouple import config

# Add your project directory to the sys.path
path = '/home/yourusername/Ai-basicscourse/ai_course_platform'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables from .env
env_path = Path(path) / '.env'
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'ai_course_platform.settings'

# Load the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
*(Make sure to replace `yourusername` with your actual PythonAnywhere username)*

3. Save the WSGI file.

## 7. Reload and Launch
1. Go back to the **Web** tab.
2. Click the green **Reload yourusername.pythonanywhere.com** button at the top.
3. Visit your site at `https://yourusername.pythonanywhere.com`!

> [!NOTE] 
> **Database:** By default, this setup uses SQLite, which is fully persistent on PythonAnywhere. If you wish to use MySQL or PostgreSQL, PythonAnywhere offers MySQL on the free tier, and PostgreSQL on paid tiers. Update the `DATABASE_URL` in your `.env` to connect to it.

# Deploying AI Basics Platform to Render

This guide provides step-by-step instructions for deploying the Django-based AI Basics course platform on Render.

## 1. Prerequisites
- A Render account (https://render.com)
- A Gemini API Key for the AI Tutor (https://aistudio.google.com/app/apikey)
- Your code pushed to a GitHub repository

## 2. Web Service Setup
1. In the Render Dashboard, click **New +** and select **Web Service**.
2. Connect your GitHub repository.
3. Configure the service:
   - **Environment:** `Python`
   - **Build Command:** `pip install -r ai_course_platform/requirements.txt && cd ai_course_platform && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command:** `cd ai_course_platform && gunicorn ai_course_platform.wsgi --workers 4 --threads 4 --log-file -`

## 3. Environment Variables
Add the following **Environment Variables** in Render:
- `SECRET_KEY`: A strong, random string
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: `*` (or your specific `.onrender.com` domain)
- `CSRF_TRUSTED_ORIGINS`: `https://your-app-name.onrender.com`
- `GEMINI_API_KEY`: Your Google Gemini API key
- `GEMINI_MODEL`: `gemini-3.6-flash`
- `PYTHON_VERSION`: `3.12`

## 4. Database
By default, the app uses SQLite. On Render, the free tier uses an ephemeral filesystem, meaning SQLite data will be wiped on restarts. 
To use a persistent PostgreSQL database:
1. Create a **PostgreSQL** instance on Render.
2. Add the `DATABASE_URL` environment variable to your Web Service with the internal database URL provided by Render.
3. Redeploy the Web Service. Django will automatically switch to PostgreSQL and run the migrations.

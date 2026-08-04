# AI Basics for Everyone

A comprehensive, dynamic learning platform built with Django to deliver AI education for total beginners — no coding or technical background required. Transform from AI literacy to building professional-grade multi-agent systems.

## 🚀 Overview

This platform is designed to bridge the gap between everyday life and work and the new era of AI-driven automation. It features a robust curriculum management system that allows for seamless integration of educational content via Markdown and JSON structures.

## ✨ Key Features

- **20+ Real-World AI Solutions**: Learn to build and deploy practical AI tools for everyday productivity, at work or in your personal life.
- **Dynamic Curriculum Loader**: Automatically synchronizes course structure from `curriculum/structure.json` and markdown files.
- **Advanced Agent Architectures**: Covers Multi-Agent systems, Function Calling, and RAG, taught through relatable, general-audience examples.
- **Interactive Dashboards**: Track progress through 10 weeks of immersive daily lessons.
- **Professional Readiness**: Focused on genuine AI fluency and future-proofing your career, whatever your field.

## 🛠️ Technology Stack

- **Backend**: Python / Django
- **Frontend**: HTML5 / Vanilla CSS
- **Content**: Markdown-driven curriculum
- **Database**: SQLite (default) / PostgreSQL
- **Config**: Python-Decouple for environment management

## 📁 Project Structure

```text
├── ai_course_platform/      # Django project & apps
│   ├── courses/             # Main course logic & models
│   ├── users/               # Authentication & profiles
│   ├── templates/           # UI components & layouts
│   └── static/              # Stylesheets and assets
├── curriculum/              # Learning material
│   ├── structure.json       # Curriculum roadmap
│   └── week1-10/            # Markdown lesson content
└── scratch/                 # Utility & automation scripts (gitignored, local-only)
```

## ⚙️ Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jpechetty-debug/AIbasics.git
   cd AIbasics
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r ai_course_platform/requirements.txt
   ```

4. **Environment Configuration**:
   Create a `.env` file in `ai_course_platform/` based on `.env.example`:
   ```bash
   cp ai_course_platform/.env.example ai_course_platform/.env
   ```
   Replace the `GEMINI_API_KEY` placeholder with a real key if you want the AI Tutor and Prompt Playground to be fully live — otherwise they gracefully report as offline.

5. **Initialize Database & Load Curriculum**:
   ```bash
   cd ai_course_platform
   python manage.py migrate
   python manage.py load_curriculum
   ```

6. **(Optional) Seed a ready-to-demo account**:
   ```bash
   python manage.py seed_demo_data
   ```
   Creates `demoadmin` / `DemoPassword123!` with all 60 lessons complete and a verifiable certificate — ideal for judges or reviewers who want to see the finished experience instantly.

7. **Run Server**:
   ```bash
   python manage.py runserver
   ```

## 🌐 Deployment

For deploying the platform to a live environment (e.g., Render), refer to the detailed [Deployment Guide](docs/deploy_render.md).

Key Production Considerations:
- **DEBUG**: Ensure `DEBUG=False` in production.
- **CSRF**: Configure `CSRF_TRUSTED_ORIGINS` for your production domain.
- **Cache**: Automatic fallback to `LocMemCache` if local Redis is missing or unreachable.
- **Frontend Assets**: Tailwind CDN used for zero-build dev velocity; compile static CSS via Tailwind CLI for production.

## 📚 Curriculum Roadmap

The course is divided into 5 strategic phases, designed for a general beginner audience:

- **Phase 1: Foundations (Weeks 1-2)**: Mastering AI/ML/DL terminology and how AI works, using everyday, relatable examples.
- **Phase 2: Prompt Engineering (Weeks 3-4)**: Industry-standard patterns (Translate, Summarize, Extract, Generate) and complex chaining.
- **Phase 3: Automation & Systems (Weeks 5-7)**: Beginner-friendly Python, everyday automation, and building RAG systems.
- **Phase 4: Capstone (Week 8)**: Building and deploying a working AI solution for a real problem of your choosing.
- **Phase 5: Professional Fluency (Weeks 9-10)**: 20+ real-world solutions and future-proofing your career, in any field.

---
*Developed with a focus on genuine accessibility and real-world usefulness for beginners everywhere.*

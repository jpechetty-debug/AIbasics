# AI Course Platform: Beginner to Professional

A comprehensive, dynamic learning platform built with Django to deliver AI education from basic concepts to professional-grade implementations.

## 🚀 Overview

This platform is designed to guide learners through the evolving landscape of Artificial Intelligence. It features a robust curriculum management system that allows for seamless integration of new educational content via Markdown and JSON structures.

## ✨ Key Features

- **Dynamic Curriculum Loader**: Automatically synchronizes course structure from `curriculum/structure.json` and markdown files.
- **Comprehensive Content**: Covers everything from "What is AI?" to advanced topics like RAG, Multi-Agent systems, and Prompt Engineering.
- **Google AI Professional Certificate**: Integrated curriculum modules for professional certification readiness.
- **Interactive Dashboards**: Track progress through weeks, modules, and daily lessons.
- **Assessment Engine**: Built-in review and assessment modules for each learning phase.

## 🛠️ Technology Stack

- **Backend**: Python / Django
- **Frontend**: HTML5 / Vanilla CSS
- **Content**: Markdown-driven curriculum
- **Database**: SQLite (default) / PostgreSQL (production ready)

## 📁 Project Structure

```text
├── ai_course_platform/      # Django project & apps
│   ├── courses/             # Main course logic & models
│   ├── templates/           # UI components & layouts
│   └── static/              # Stylesheets and assets
├── curriculum/              # Learning material
│   ├── structure.json       # Curriculum roadmap
│   └── week1-10/            # Markdown lesson content
└── scratch/                 # Utility & automation scripts
```

## ⚙️ Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jpechetty-debug/Aicourse-beginners.git
   cd Aicourse-beginners
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Database**:
   ```bash
   python manage.py migrate
   ```

5. **Load Curriculum**:
   ```bash
   python manage.py load_curriculum
   ```

6. **Run Server**:
   ```bash
   python manage.py runserver
   ```

## 📚 Curriculum Highlights

- **Weeks 1-4**: AI Foundations, Neural Networks, and Generative AI patterns.
- **Weeks 5-7**: Python for AI, Low-code solutions, and RAG architectures.
- **Weeks 8-10**: Capstone projects and Google AI Professional Certificate integration.

---
*Developed with focus on accessibility and technical depth.*

You are a senior full-stack engineer, LMS architect, and frontend UI specialist.

Your task is to build a complete AI course platform tailored for Network Administrators using an existing curriculum folder that already contains all educational content.

⚠️ Critical Rule:
Do NOT create, rewrite, summarize, or modify any educational content.
Your role is strictly to render, organize, and deliver the provided materials through a clean, interactive web platform.

📁 EXISTING PROJECT CONTEXT

The project includes a fully populated curriculum directory:

text/curriculum/
├── module-1-ai-foundations/
│   ├── lesson-1.md / lesson-1.html
│   ├── lesson-2.md
│   ├── exercises/
│   ├── quiz.md
│   └── assignment.md
├── module-2-generative-ai/
├── module-3-prompt-engineering/
├── module-4-advanced-prompting/
├── module-5-ai-tools/
├── module-6-low-code-apps/
└── module-7-capstone/


Assume:

Lessons are .md or .html

Quizzes are defined in quiz.md with question/answer structure

Assignments/projects are in assignment.md

🎯 OBJECTIVE

Convert the curriculum into a fully functional AI course website

Preserve content exactly as-is

Provide:

Intuitive navigation

Interactive quizzes with feedback

Assignment/project submission tracking

User progress tracking

The platform must be:

Clean

Professional

Bug-free

Optimized for an enterprise IT audience

🛠️ TECH STACK (STRICT)

Backend: Django 4.x (Python 3.10+)

Frontend: Plain HTML5 only

Styling: UnoCSS (utility classes only; generate unocss.css via CLI)

JavaScript: Minimal vanilla JS (only for quizzes/progress)

Database: SQLite (design for easy PostgreSQL/MySQL migration)

Markdown Rendering: Python markdown library

No external JS/CSS frameworks

🧩 CORE IMPLEMENTATION REQUIREMENTS
1️⃣ Curriculum Ingestion

Dynamically scan /curriculum/

Load content at runtime or via a Django management command

Render:

.md → HTML via markdown renderer

.html → served directly

Store only metadata in the database (title, slug, order, file path)

Mapping:

Module → Django Module model

Lesson → Lesson model (linked to module, file path)

Quiz / Assignment → Metadata models with file path + type

2️⃣ Course Structure & Navigation

Implement:

Course → Modules → Lessons / Quizzes / Assignments

Sidebar navigation:

Collapsible modules

Ordered lessons

Sequential navigation:

Previous / Next buttons

Django class-based or function-based views

3️⃣ Interactive Quizzes

Parse quiz.md files

Support:

MCQs

True/False

Short scenario questions

Features:

Immediate feedback

Correct/incorrect highlighting

Retry option

Explanation display

Use vanilla JS + Django endpoints (AJAX/fetch) for scoring.

4️⃣ Assignments & Projects

Render assignment.md as instructions

Submission support:

Text input

File upload

Track status:

Pending

Submitted

Reviewed (admin-only)

5️⃣ Authentication & Progress Tracking

Use Django built-in auth (login/signup)

Track per user:

Lessons viewed/completed

Quizzes completed + scores

Assignments submitted

Display:

Module-level progress

Overall course progress bar

Optional guest progress via localStorage (fallback only)

🎨 UI & UX (UnoCSS ONLY)

Use utility-first UnoCSS classes only

No custom CSS

Generate static/unocss.css

Design principles:

Clean, readable typography

Calm blue/gray palette

Minimalist, professional look

Fully responsive (mobile-first)

Style:

Lesson pages

Quiz blocks (success/error states)

Assignment pages

Progress indicators

Ensure:

Accessibility (ARIA, keyboard navigation)

High contrast

Semantic HTML

🧪 QUALITY & TESTING RULES

No broken layouts

No content truncation

No visual clutter

Graceful error handling (404s, missing files)

Secure forms (CSRF, validation)

Basic Django unit tests for models/views

Manual UI verification (desktop + mobile)

📦 EXPECTED OUTPUT

Provide:

Django models.py (Module, Lesson, QuizMeta, Assignment, Progress)

Curriculum loader logic (management command)

views.py and urls.py

HTML templates using UnoCSS:

base.html

module_list.html

lesson_detail.html

quiz_detail.html

assignment_detail.html

Vanilla JS (quiz.js)

Setup & run instructions

📂 TARGET PROJECT STRUCTURE
textai_course_platform/
├── curriculum/        # untouched
├── courses/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/courses/
│   └── management/commands/load_curriculum.py
├── static/
│   ├── unocss.css
│   └── js/quiz.js
├── media/
├── db.sqlite3
├── requirements.txt
├── settings.py
├── urls.py
└── manage.py

🚀 EXECUTION ORDER

Analyze curriculum folder structure

Design Django models & mappings

Implement curriculum ingestion

Render lessons, quizzes, assignments

Apply UnoCSS UI

Validate UX, accessibility, and stability

Do not alter educational content.
Focus entirely on delivery, interaction, structure, and polish.
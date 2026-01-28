"""
Management command to load curriculum content from markdown files.
"""
import os
import re
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.text import slugify
from courses.models import Module, Lesson


class Command(BaseCommand):
    help = 'Load curriculum content from markdown files into the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing modules and lessons before loading',
        )

    def handle(self, *args, **options):
        curriculum_dir = settings.CURRICULUM_DIR
        
        if not curriculum_dir.exists():
            self.stderr.write(self.style.ERROR(f'Curriculum directory not found: {curriculum_dir}'))
            return

        if options['clear']:
            self.stdout.write('Clearing existing data...')
            Lesson.objects.all().delete()
            Module.objects.all().delete()

        self.stdout.write(f'Loading curriculum from: {curriculum_dir}')
        
        # Get all week directories
        week_dirs = sorted([
            d for d in curriculum_dir.iterdir()
            if d.is_dir() and d.name.startswith('week')
        ], key=lambda x: int(re.search(r'\d+', x.name).group()))

        for week_index, week_dir in enumerate(week_dirs, start=1):
            module = self.create_module(week_dir, week_index)
            self.load_lessons(module, week_dir)

        total_modules = Module.objects.count()
        total_lessons = Lesson.objects.count()
        
        self.stdout.write(self.style.SUCCESS(
            f'Successfully loaded {total_modules} modules and {total_lessons} lessons'
        ))

    def create_module(self, week_dir, order):
        """Create or update a module from a week directory."""
        folder_name = week_dir.name
        week_num = int(re.search(r'\d+', folder_name).group())
        
        # Read the first lesson to extract module topic
        lesson_files = sorted([
            f for f in week_dir.iterdir()
            if f.is_file() and f.suffix == '.md' and not f.name.startswith('week')
        ])
        
        title = f"Week {week_num}"
        description = ""
        
        if lesson_files:
            first_lesson = lesson_files[0]
            lesson_title = self.extract_title(first_lesson)
            if lesson_title:
                # Create a more descriptive module title based on content
                title = self.get_module_title(week_num, lesson_files)
        
        module, created = Module.objects.update_or_create(
            folder_name=folder_name,
            defaults={
                'title': title,
                'slug': slugify(f"week-{week_num}"),
                'description': description,
                'order': order,
            }
        )
        
        action = 'Created' if created else 'Updated'
        self.stdout.write(f'  {action} module: {module.title}')
        return module

    def get_module_title(self, week_num, lesson_files):
        """Generate a descriptive module title based on lesson content."""
        week_titles = {
            1: "AI Foundations",
            2: "How AI Works",
            3: "Prompt Patterns",
            4: "Advanced Prompting",
            5: "AI for Scripting",
            6: "Low-Code AI Apps",
            7: "AI Agents & Tools",
            8: "Capstone Project",
        }
        return f"Week {week_num}: {week_titles.get(week_num, 'AI Training')}"

    def load_lessons(self, module, week_dir):
        """Load all lesson files from a week directory."""
        md_files = sorted([
            f for f in week_dir.iterdir()
            if f.is_file() and f.suffix == '.md'
        ])
        
        lesson_order = 0
        for md_file in md_files:
            # Skip UIprompt or other non-content files
            if 'prompt' in md_file.name.lower() and 'ui' in md_file.name.lower():
                continue
                
            lesson_order += 1
            self.create_lesson(module, md_file, lesson_order)

    def create_lesson(self, module, file_path, order):
        """Create or update a lesson from a markdown file."""
        title = self.extract_title(file_path)
        if not title:
            title = self.generate_title_from_filename(file_path.name)
        
        # Determine content type
        content_type = 'assessment' if 'assessment' in file_path.name else 'lesson'
        
        # Use relative path from curriculum directory
        relative_path = file_path.relative_to(settings.CURRICULUM_DIR)
        
        lesson, created = Lesson.objects.update_or_create(
            module=module,
            file_path=str(relative_path),
            defaults={
                'title': title,
                'slug': slugify(title)[:300],
                'content_type': content_type,
                'order': order,
            }
        )
        
        action = 'Created' if created else 'Updated'
        self.stdout.write(f'    {action} lesson: {lesson.title}')

    def extract_title(self, file_path):
        """Extract the title from a markdown file's first heading."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('# '):
                        return line[2:].strip()
        except Exception as e:
            self.stderr.write(f'Error reading {file_path}: {e}')
        return None

    def generate_title_from_filename(self, filename):
        """Generate a readable title from a filename."""
        # Remove extension
        name = Path(filename).stem
        # Replace underscores with spaces
        name = name.replace('_', ' ')
        # Remove leading numbers/day prefixes
        name = re.sub(r'^day\d+\s*', '', name, flags=re.IGNORECASE)
        name = re.sub(r'^week\d+\s*', '', name, flags=re.IGNORECASE)
        # Title case
        return name.title()

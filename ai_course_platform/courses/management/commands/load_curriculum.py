"""
Management command to load curriculum content from markdown files.
"""
import os
import re
import json
import frontmatter
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
        structure_file = curriculum_dir / 'structure.json'
        
        if not curriculum_dir.exists():
            self.stderr.write(self.style.ERROR(f'Curriculum directory not found: {curriculum_dir}'))
            return

        # Load structure manifest if it exists
        structure_data = {}
        if structure_file.exists():
            with open(structure_file, 'r', encoding='utf-8') as f:
                structure_data = json.load(f)
            self.stdout.write(self.style.SUCCESS(f"Loaded structure manifest: {structure_data.get('course_title')}"))

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
            module = self.create_module(week_dir, week_index, structure_data)
            self.load_lessons(module, week_dir)

        total_modules = Module.objects.count()
        total_lessons = Lesson.objects.count()
        
        self.stdout.write(self.style.SUCCESS(
            f'Successfully loaded {total_modules} modules and {total_lessons} lessons'
        ))

    def create_module(self, week_dir, order, structure_data):
        """Create or update a module from a week directory."""
        folder_name = week_dir.name
        week_num_str = re.search(r'\d+', folder_name).group()
        week_num = int(week_num_str)
        
        # Default title
        title = f"Week {week_num}"
        description = ""
        phase_title = ""
        phase_id = ""

        # Get details from structure.json if available
        week_info = structure_data.get('week_details', {}).get(week_num_str)
        if week_info:
            title = f"Week {week_num}: {week_info.get('title', '')}"
            description = week_info.get('summary', '')

        # Determine phase
        for phase in structure_data.get('phases', []):
            if week_num in phase.get('weeks', []):
                phase_title = phase.get('title', '')
                phase_id = phase.get('id', '')
                break
        
        module, created = Module.objects.update_or_create(
            folder_name=folder_name,
            defaults={
                'title': title,
                'slug': slugify(f"week-{week_num}"),
                'description': description,
                'phase_title': phase_title,
                'phase_id': phase_id,
                'order': order,
            }
        )
        
        action = 'Created' if created else 'Updated'
        self.stdout.write(f'  {action} module: {module.title} ({phase_id})')
        return module

    def load_lessons(self, module, week_dir):
        """Load all lesson files from a week directory."""
        md_files = sorted([
            f for f in week_dir.iterdir()
            if f.is_file() and f.suffix == '.md'
        ])
        
        lesson_order = 0
        for md_file in md_files:
            # Skip non-content files
            if 'prompt' in md_file.name.lower() and 'ui' in md_file.name.lower():
                continue
                
            lesson_order += 1
            self.create_lesson(module, md_file, lesson_order)

    def create_lesson(self, module, file_path, order):
        """Create or update a lesson from a markdown file."""
        # Use frontmatter to extract metadata
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            title = post.get('title')
            difficulty = post.get('difficulty', '')
            duration = post.get('duration', '')
            replit_url = post.get('replit_url', '')
            codespaces_url = post.get('codespaces_url', '')
            
            if not title:
                title = self.extract_title_from_content(post.content) or self.generate_title_from_filename(file_path.name)
        except Exception as e:
            self.stderr.write(f'Error reading frontmatter from {file_path}: {e}')
            title = self.generate_title_from_filename(file_path.name)
            difficulty = ''
            duration = ''
            replit_url = ''
            codespaces_url = ''
        
        # Determine content type
        content_type = 'assessment' if 'assessment' in file_path.name else 'lesson'
        
        # Use relative path from curriculum directory
        relative_path = file_path.relative_to(settings.CURRICULUM_DIR)
        
        lesson, created = Lesson.objects.update_or_create(
            module=module,
            file_path=relative_path.as_posix(),
            defaults={
                'title': title,
                'slug': slugify(title)[:300],
                'content_type': content_type,
                'difficulty': difficulty,
                'duration': duration,
                'replit_url': replit_url,
                'codespaces_url': codespaces_url,
                'order': order,
            }
        )
        
        action = 'Created' if created else 'Updated'
        self.stdout.write(f'    {action} lesson: {lesson.title} [{difficulty}, {duration}]')

    def extract_title_from_content(self, content):
        """Extract the title from a markdown string's first heading."""
        for line in content.splitlines():
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
        return None

    def generate_title_from_filename(self, filename):
        """Generate a readable title from a filename."""
        name = Path(filename).stem
        name = name.replace('_', ' ')
        name = re.sub(r'^day\d+\s*', '', name, flags=re.IGNORECASE)
        name = re.sub(r'^week\d+\s*', '', name, flags=re.IGNORECASE)
        return name.title()

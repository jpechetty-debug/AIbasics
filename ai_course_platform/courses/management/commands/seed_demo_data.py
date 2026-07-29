"""
Management command to seed demo data for hackathon judging and live demonstrations.
Creates demo user, marks curriculum progress complete, and issues a deterministic UUID certificate.
"""
import uuid
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User
from courses.models import Module, Lesson, UserProgress, Certificate


class Command(BaseCommand):
    help = "Seed demo user, complete progress, and issue verifiable certificate for judging."

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("--- Seeding Demo Environment ---"))

        # 1. Load curriculum if not already populated
        if Lesson.objects.count() == 0:
            self.stdout.write("Loading curriculum data...")
            call_command("load_curriculum")

        # 2. Create demo user
        demo_user, created = User.objects.get_or_create(
            username="demoadmin",
            defaults={
                "email": "demo@example.com",
                "first_name": "Demo",
                "last_name": "Judge",
                "is_staff": True,
                "is_superuser": True
            }
        )
        demo_user.set_password("DemoPassword123!")
        demo_user.save()

        if created:
            self.stdout.write(self.style.SUCCESS("[OK] Created demo user: demoadmin / DemoPassword123!"))
        else:
            self.stdout.write("[OK] Demo user 'demoadmin' updated.")

        # 3. Mark all lessons completed for demo user
        lessons = Lesson.objects.all()
        progress_records = [
            UserProgress(user=demo_user, lesson=lesson, completed=True)
            for lesson in lessons
        ]
        UserProgress.objects.filter(user=demo_user).delete()
        UserProgress.objects.bulk_create(progress_records)
        self.stdout.write(self.style.SUCCESS(f"[OK] Marked {len(lessons)} lessons complete for 'demoadmin'."))

        # 4. Issue deterministic Certificate
        demo_uuid = uuid.UUID("11111111-2222-3333-4444-555555555555")
        cert, cert_created = Certificate.objects.get_or_create(
            user=demo_user,
            defaults={"verification_uuid": demo_uuid}
        )
        if not cert_created and cert.verification_uuid != demo_uuid:
            cert.verification_uuid = demo_uuid
            cert.save()

        self.stdout.write(self.style.SUCCESS(f"[OK] Issued Certificate UUID: {demo_uuid}"))
        
        self.stdout.write("============================================================")
        self.stdout.write(self.style.SUCCESS("DEMO ENVIRONMENT READY FOR JUDGING:"))
        self.stdout.write(f"  - Demo User Login: demoadmin / DemoPassword123!")
        self.stdout.write(f"  - Dashboard URL: http://127.0.0.1:8000/")
        self.stdout.write(f"  - Grounded Lesson: http://127.0.0.1:8000/lesson/{lessons.first().pk if lessons.exists() else 1}/")
        self.stdout.write(f"  - Prompt Playground: http://127.0.0.1:8000/prompt-playground/")
        self.stdout.write(f"  - Verifiable Cert URL: http://127.0.0.1:8000/verify/{demo_uuid}/")
        self.stdout.write("============================================================\n")

"""
Unit tests for course views, authentication, progress, and certificates.
"""
import json
from unittest.mock import patch, MagicMock
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from courses.models import Module, Lesson, UserProgress, Certificate


class CourseViewsTest(TestCase):
    """Test suite for course views and access controls."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testadmin', password='Password123!')
        self.module = Module.objects.create(
            title='Module 1: Foundations',
            slug='module-1-foundations',
            order=1,
            folder_name='week1'
        )
        self.lesson = Lesson.objects.create(
            module=self.module,
            title='Day 1: What is AI',
            slug='day-1-what-is-ai',
            file_path='week1/day1_what_is_ai.md',
            content_type='lesson',
            order=1
        )

    def test_dashboard_renders_for_guest(self):
        """Dashboard should render for guest users without error."""
        response = self.client.get(reverse('courses:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Get Good at AI')

    def test_lesson_detail_login_required(self):
        """Unauthenticated user accessing a lesson should be redirected to login."""
        url = reverse('courses:lesson_detail', kwargs={'pk': self.lesson.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/users/login/', response.url)

    def test_authenticated_user_can_access_lesson(self):
        """Authenticated user can view lesson details."""
        self.client.login(username='testadmin', password='Password123!')
        url = reverse('courses:lesson_detail', kwargs={'pk': self.lesson.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_mark_lesson_complete_ajax(self):
        """Authenticated user can mark a lesson complete via POST API."""
        self.client.login(username='testadmin', password='Password123!')
        url = reverse('courses:mark_complete', kwargs={'pk': self.lesson.pk})
        response = self.client.post(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        
        progress = UserProgress.objects.get(user=self.user, lesson=self.lesson)
        self.assertTrue(progress.completed)

    def test_certificate_issuance_and_verification(self):
        """Completing all lessons grants a certificate with a valid UUID verification URL."""
        UserProgress.objects.create(user=self.user, lesson=self.lesson, completed=True)
        
        self.client.login(username='testadmin', password='Password123!')
        cert_url = reverse('courses:certificate')
        response = self.client.get(cert_url)
        self.assertEqual(response.status_code, 200)
        
        cert = Certificate.objects.get(user=self.user)
        verify_url = reverse('courses:verify_certificate', kwargs={'uuid': cert.verification_uuid})
        
        # Verify public access without login
        guest_client = Client()
        verify_response = guest_client.get(verify_url)
        self.assertEqual(verify_response.status_code, 200)
        self.assertContains(verify_response, 'Cryptographically Verified Credential')

    def test_prompt_playground_get(self):
        """Prompt Playground GET page renders for authenticated user."""
        self.client.login(username='testadmin', password='Password123!')
        url = reverse('courses:prompt_playground')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Prompt Playground')

    def test_prompt_playground_post_validation(self):
        """Prompt Playground POST rejects oversized system prompts exceeding 2000 chars."""
        self.client.login(username='testadmin', password='Password123!')
        url = reverse('courses:prompt_playground')
        response = self.client.post(
            url,
            data={'system': 'A' * 2005, 'prompt': 'Hello'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn('System prompt too long', response.json()['error'])

    def test_ai_tutor_success_with_mock(self):
        """AI Tutor POST returns successful JSON response when client is configured."""
        self.client.login(username='testadmin', password='Password123!')
        url = reverse('courses:ai_tutor', kwargs={'pk': self.lesson.pk})
        with patch('courses.views.get_gemini_client') as mock_get_client:
            mock_client = MagicMock()
            # Mock the structure of Gemini API response
            mock_response = MagicMock()
            mock_response.text = "This is a mock response from Gemini API."
            mock_client.models.generate_content.return_value = mock_response
            mock_get_client.return_value = mock_client
            
            response = self.client.post(
                url,
                data=json.dumps({'query': 'What is a neural network?'}),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.content)
            self.assertTrue(data.get('success'))
            self.assertIn('mock response', data.get('response'))

    def test_prompt_playground_success_with_mock(self):
        """Prompt Playground POST returns successful response when client is configured."""
        self.client.login(username='testadmin', password='Password123!')
        url = reverse('courses:prompt_playground')
        with patch('courses.views.get_gemini_client') as mock_get_client:
            mock_client = MagicMock()
            mock_response = MagicMock()
            mock_response.text = "Playground mock response."
            mock_client.models.generate_content.return_value = mock_response
            mock_get_client.return_value = mock_client
            
            payload = {
                'prompt': 'Write a haiku about AI.',
                'system': 'You are a poet.'
            }
            response = self.client.post(
                url,
                data=json.dumps(payload),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.content)
            self.assertTrue(data.get('success'))
            self.assertIn('Playground mock response.', data.get('response'))

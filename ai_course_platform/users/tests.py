"""
Unit tests for user authentication, registration, login, and open-redirect prevention.
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class UserAuthViewsTest(TestCase):
    """Test suite for user authentication flows."""

    def setUp(self):
        self.client = Client()
        self.username = 'authuser'
        self.password = 'SecurePass123!'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_register_page_renders(self):
        """Register GET view renders form."""
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)

    def test_register_new_user(self):
        """Register POST creates new user and logs them in."""
        response = self.client.post(reverse('users:register'), {
            'username': 'newstudent',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newstudent').exists())

    def test_login_valid_credentials(self):
        """Login POST with valid credentials redirects to dashboard."""
        response = self.client.post(reverse('users:login'), {
            'username': self.username,
            'password': self.password,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('courses:dashboard'))

    def test_login_open_redirect_prevention(self):
        """Malicious external next_url parameter must be rejected and redirected safely."""
        response = self.client.post(f"{reverse('users:login')}?next=https://malicious-site.com", {
            'username': self.username,
            'password': self.password,
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('courses:dashboard'))

    def test_logout_user(self):
        """Logout POST logs out the authenticated user."""
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('courses:dashboard'))

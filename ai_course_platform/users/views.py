"""
Views for user authentication.
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.views import View


class RegisterView(View):
    """User registration view."""
    template_name = 'users/register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('courses:dashboard')
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Your account has been created.')
            return redirect('courses:dashboard')
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    """User login view."""
    template_name = 'users/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('courses:dashboard')
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            next_url = request.GET.get('next', 'courses:dashboard')
            return redirect(next_url)
        return render(request, self.template_name, {'form': form})


def logout_view(request):
    """Log out the user."""
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('courses:dashboard')

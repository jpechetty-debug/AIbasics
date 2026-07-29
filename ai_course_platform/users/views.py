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


from django.utils.http import url_has_allowed_host_and_scheme


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
            next_url = request.GET.get('next') or request.POST.get('next')
            if next_url and url_has_allowed_host_and_scheme(url=next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)
            return redirect('courses:dashboard')
        return render(request, self.template_name, {'form': form})


from django.views.decorators.http import require_POST

@require_POST
def logout_view(request):
    """Log out the user."""
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('courses:dashboard')

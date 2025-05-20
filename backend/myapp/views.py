from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework_api_key.models import APIKey
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render
from .forms import CreateUserForm
from django.contrib.auth.views import LogoutView


class MyLogoutView(LogoutView):
    next_page = '/api/'  # Redirect to this page after logout


def home(request):
    return render(request, 'home.html')


class RevokeKeyView(LoginRequiredMixin, View):
    def post(self, request):
        key_id = request.POST.get('key_id')
        APIKey.objects.filter(id=key_id, name__startswith=f"{request.user.username}-").delete()
        messages.success(request, "API key revoked.")
        return redirect('developer-portal')


class RegisterView(CreateView):
    form_class = CreateUserForm
    template_name = 'developer_portal/register.html'
    success_url = reverse_lazy('login')


class DeveloperPortalView(LoginRequiredMixin, TemplateView):
    template_name = 'developer_portal/portal.html'

    def post(self, request):
        # Generate a new API key
        api_key, key = APIKey.objects.create_key(name=f"{request.user.username}-{request.user.id}")
        messages.success(request, f"New API key created: {key}")
        return self.get(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get user's API keys
        context['api_keys'] = APIKey.objects.filter(name__startswith=f"{self.request.user.username}-")
        return context


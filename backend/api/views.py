from .models import CustomUser, Book
from .serializers import UserSerializer, BookSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
import json
import os
from django.conf import settings
from rest_framework_api_key.models import APIKey
from rest_framework.authentication import SessionAuthentication
from django.http import JsonResponse
from django.middleware.csrf import get_token


def csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})


class PublicAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'message': 'This is a public endpoint'})


class BookListAPIView(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]  # Require API key for this view
    serializer_class = BookSerializer
    throttle_scope = 'api'

    def get_queryset(self):
        queryset = Book.objects.all()
        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset


class Home(APIView):
    def get(self, request):
        data = {'message': 'Hello, World!'}
        return Response(data)


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'developer_portal/register.html'
    success_url = reverse_lazy('login')


class DeveloperPortalView(LoginRequiredMixin, TemplateView):
    template_name = 'developer_portal/portal.html'

    def post(self, request):
        api_key, key = APIKey.objects.create_key(name=f"{request.user.username}-{request.user.id}")
        messages.success(request, f"New API key created: {key}")
        return self.get(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['api_keys'] = APIKey.objects.filter(name__startswith=f"{self.request.user.username}-")
        return context


# New view for user-based auth
class ProfileAPI(APIView):
    permission_classes = [IsAuthenticated]  # Require user authentication
    # authentication_classes = [SessionAuthentication]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
            'id': user.id,
        })


'''
class BookListAPIView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(title__icontains=query)
        return Book.objects.all()

'''


def home(request):
    return Response({
        "Welcome to our API"
    })


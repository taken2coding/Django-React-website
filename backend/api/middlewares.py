# myproject/middleware.py
from rest_framework_api_key.models import APIKey
from django.db.models import Count
from datetime import datetime, timedelta


class APILogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.META.get('HTTP_AUTHORIZATION', '').replace('Api-Key ', '')
        if api_key:
            try:
                key = APIKey.objects.get_from_key(api_key)
                # Log request (simplified)
                print(f"{datetime.now()}: {key.name} accessed {request.path}")
            except APIKey.DoesNotExist:
                pass
        return self.get_response(request)
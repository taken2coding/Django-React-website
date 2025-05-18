from django.contrib import admin
from django.urls import path, include
'''
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]


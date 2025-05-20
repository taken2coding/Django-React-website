from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from .views import RegisterView,RevokeKeyView, DeveloperPortalView, home,  MyLogoutView
from django.contrib.auth.views import LoginView, LogoutView


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
    path('', TemplateView.as_view(template_name='index.html'), name="home"),
    # Authentication routes
    path('developer-portal/login/', LoginView.as_view(template_name='developer_portal/login.html'), name='login'),
    path('developer-portal/logout/',  MyLogoutView.as_view(), name='logout'),
    path('developer-portal/register/', RegisterView.as_view(), name='register'),
    path('developer-portal/', DeveloperPortalView.as_view(), name='developer-portal'),
    path('developer-portal/revoke/', RevokeKeyView.as_view(), name='revoke-key'),
    re_path(r'^(?!static/|api/|admin/|developer-portal/).*$', home, name='catch-all'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index
from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', IndexView.as_view(), name='index'),
    path('', index, name='index'),  # Serve React app at root
    path('api/', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # re_path(r'^.*$', IndexView.as_view(), name='index'),  # Catch-all for React Router
]

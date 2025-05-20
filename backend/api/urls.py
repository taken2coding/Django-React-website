from .views import ProfileAPI, BookListAPIView, Home,PublicAPI, DeveloperPortalView, RegisterView, ProfileAPI,csrf_token
from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/', ProfileAPI.as_view(), name='user_profile'),
    path('books/', BookListAPIView.as_view({'get': 'list'}), name='book_list'),
    path('public/', PublicAPI.as_view(), name='public-api'),
    # JWT token endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('developer-portal/login/', LoginView.as_view(template_name='developer_portal/login.html'), name='login'),
    # path('developer-portal/logout/', LogoutView.as_view(), name='logout'),
    # path('developer-portal/register/', RegisterView.as_view(), name='register'),
    # path('developer-portal/', DeveloperPortalView.as_view(), name='developer-portal'),
    # path('api/csrf/', csrf_token, name='csrf'),
    # React frontend
]
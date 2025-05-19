from django.urls import path
from .views import UserProfileView, BookListAPIView, Home


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('books/', BookListAPIView.as_view({'get': 'list'}), name='book_list'),
]
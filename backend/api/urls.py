from django.urls import path
from .views import UserProfileView, SampleAPI

urlpatterns = [
    path('sample/', SampleAPI.as_view(), name='sample-api'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]
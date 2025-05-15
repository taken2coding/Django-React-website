from django.contrib import admin
from .models import CustomUser, UserProfile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ('username',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

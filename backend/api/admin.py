from django.contrib import admin
from .models import CustomUser, UserProfile, Book
from rest_framework_api_key.models import APIKey


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ('username',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author',)
    search_fields = ('title','author',)


# admin.site.register(APIKey)

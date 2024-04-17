# hotel_app/admin.py

from django.contrib import admin
from .models import Room, Category, Meal, Comment, Bed


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'text']

@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ['name']




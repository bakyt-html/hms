# hotel_app/admin.py

from django.contrib import admin
from .models import Room, RoomPhoto

# Регистрируем модель Room для административной панели
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity']  # Отображаемые поля в списке объектов

# Регистрируем модель RoomPhoto для административной панели
@admin.register(RoomPhoto)
class RoomPhotoAdmin(admin.ModelAdmin):
    pass  # Пока не указываем дополнительных настроек, но можно добавить позже

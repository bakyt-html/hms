from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    capacity = models.IntegerField(verbose_name='Количество мест')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='фото', upload_to='room_images/')
    price = models.IntegerField(verbose_name='цена', default=1000)

    def __str__(self):
        return self.name

class RoomPhoto(models.Model):
    room = models.ForeignKey('Room', related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='room_photos/')

    def __str__(self):
        return f'Photo of {self.room.name}'


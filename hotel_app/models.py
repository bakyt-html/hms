from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    capacity = models.IntegerField(verbose_name='Количество мест')
    description = models.TextField(verbose_name='Описание')
    image_1 = models.ImageField(verbose_name='фото', upload_to='room_images/', null=True, blank=True)
    image_2 = models.ImageField(verbose_name='фото', upload_to='room_images/', null=True, blank=True)
    image_3 = models.ImageField(verbose_name='фото', upload_to='room_images/', null=True, blank=True)
    image_4 = models.ImageField(verbose_name='фото', upload_to='room_images/', null=True, blank=True)
    price = models.IntegerField(verbose_name='цена', default=1000)
    wifi = models.BooleanField(verbose_name='Вай-фай', default=False, )
    size = models.IntegerField(verbose_name='Размер комнаты', null=True, blank=True)
    tv = models.BooleanField(verbose_name='Телевизор', null=True, blank=True, default=False)
    air_conditioner = models.BooleanField(verbose_name='Кондиционер', null=True, blank=True, default=False)
    fan = models.BooleanField(verbose_name='Фен', null=True, blank=True, default=False)
    shower = models.BooleanField(verbose_name='Душ', null=True, blank=True, default=False)
    meal = models.ForeignKey('Meal', on_delete=models.PROTECT, verbose_name='Питание')
    beds = models.ForeignKey('Bed', on_delete=models.PROTECT, verbose_name='Кровать')
    cats = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')


    def __str__(self):
        return self.name

class Bed(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')

    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.CharField(max_length=100, verbose_name='пользователь')
    text = models.TextField(verbose_name='комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')

    def __str__(self):
        return f'{self.user}_{self.text}'

from django.db import models


class MenuItem(models.Model):
    """Меню"""
    title = models.CharField('Название', max_length=70)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='images')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0)

    TYPE =[
        ('BRK', 'Завтрак'),
        ('LUN', 'Обед'),
        ('DIN', 'Ужин'),
    ]

    type = models.CharField('Тип', choices=TYPE, default='BRk', max_length=3)

    def __str__(self):
        return self.title
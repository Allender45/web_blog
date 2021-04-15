from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')
    text = models.TextField(max_length=1500, verbose_name='Текст статьи')
    image = models.ImageField(upload_to='media/%Y%m%d/', verbose_name='Изображение')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

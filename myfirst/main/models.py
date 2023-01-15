from django.db import models

class Task(models.Model):
    Category=[("5", '5класс'),("6", '6класс')]
    article_type = models.CharField(max_length=2, choices=Category, default='', blank=True)
    title = models.CharField('Название', max_length = 50)
    task = models.TextField('Описание')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Location(models.Model):
    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    name = models.CharField(max_length=256, verbose_name='Название Места')
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлено')


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    title = models.CharField(max_length=256,
                             verbose_name='Заголовок')
    description = models.TextField(default='',
                                   verbose_name='Описание')
    slug = models.SlugField(default='', unique=True,
                            verbose_name='Идентификатор',
                            help_text='Идентификатор страницы для URL; '
                                      'разрешены символы латиницы, '
                                      'цифры, дефис и подчёркивание.')
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано',
                                       help_text='Снимите галочку, '
                                                 'чтобы скрыть публикацию.')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлено')


class Post(models.Model):
    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    title = models.CharField(max_length=256)
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(verbose_name='Дата и время публикации',
                                    help_text='Если установить дату и время в '
                                              'будущем — '
                                              'можно делать отложенные '
                                              'публикации.')
    author = models.ForeignKey(
        User,
        verbose_name='Автор публикации',
        on_delete=models.CASCADE
    )
    location = models.ForeignKey(
        Location,
        verbose_name='Местоположение',
        null=True,
        on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True
    )
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлено')

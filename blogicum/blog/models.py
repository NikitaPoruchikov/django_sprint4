from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from .constants import MAX_LENGTH_NAME
from .mixins import PublishedMixin, UserRelatedMixin


class Location(PublishedMixin):
    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name='Название места'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Category(PublishedMixin):
    title = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор'
    )

    def __str__(self):
        return f'"{self.title}" - {self.description}...'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Post(PublishedMixin, UserRelatedMixin):
    title = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name='Заголовок'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    image = models.ImageField(
        upload_to='post_images/',
        blank=True,
        verbose_name='Фото'
    )
    pub_date = models.DateTimeField(
        default=timezone.now,  # Автоматическая установка текущего времени
        verbose_name='Дата публикации'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение',
        related_name='posts'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
        related_name='posts'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts')

    def __str__(self):
        return f'{self.title} ({self.pub_date.strftime("%Y-%m-%d")})'

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date', 'title']


class Comment(PublishedMixin, UserRelatedMixin):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост'
    )
    text = models.TextField(
        verbose_name='Текст комментария'
    )

    def __str__(self):
        return f'{self.author.username}: {self.text[:50]}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created_at']

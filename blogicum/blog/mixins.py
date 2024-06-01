from django.db import models


class PublishedMixin(models.Model):
    """Абстрактная модель для полей is_published и created_at."""

    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        verbose_name='Добавлено',
        auto_now_add=True
    )

    class Meta:
        abstract = True


class UserRelatedMixin(models.Model):
    """Абстрактная модель для добавления поля 'author' к моделям."""

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name="%(class)s_posts"
    )

    class Meta:
        abstract = True

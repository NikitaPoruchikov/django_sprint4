from functools import wraps

from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils import timezone

from .models import Post


def check_post_access(func):
    """
    Декоратор для проверки доступа к посту по статусу публикации и владельцу.

    Вызывает Http404, если пост не доступен.
    """
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        now = timezone.now()

        # Проверка условий доступа к посту
        conditions = (
            post.is_published,
            post.category.is_published,
            post.pub_date <= now
        )
        if not all(conditions) and post.author != request.user:
            raise Http404("Пост не найден или не доступен.")
        return func(request, *args, **kwargs)
    return wrapper

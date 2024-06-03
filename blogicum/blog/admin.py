from django.contrib import admin

from .models import Category, Location, Post, Comment


class PostInLine(admin.TabularInline):
    model = Post
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (PostInLine,)
    list_display = (
        'title',
        'description',
        'is_published',
    )
    list_editable = ('is_published',)
    search_fields = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'text',
        'author',
        'is_published',
    )
    list_editable = ('is_published',)
    list_filter = ('is_published',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = (PostInLine,)
    list_display = (
        'name',
        'is_published',
    )
    list_editable = ('is_published',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'text',
        'author',
        'location',
        'category',
        'is_published',
    )
    list_editable = (
        'is_published',
        'pub_date',
    )
    search_fields = ('title',)
    list_filter = ('is_published',)
    list_display_links = ('title',)

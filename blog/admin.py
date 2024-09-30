from django.contrib import admin
from blog.models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'author', 'body', 'publish', 'created', 'updated', 'status']
    list_filter = ['status', 'created', 'publish']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'email', 'body', 'created', 'updated', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
    # raw_id_fields = ['post']
    # date_hierarchy = 'created'
    # ordering = ['created', 'active']
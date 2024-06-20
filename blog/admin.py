from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Comment, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'category', 'status', 'created_on', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'updated_on', 'category')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user__username', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

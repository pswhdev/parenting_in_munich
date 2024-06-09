from django.contrib import admin
from .models import Post, Category
from django.db import IntegrityError
from django.contrib import messages
from django.utils.text import slugify
from django_summernote.admin import SummernoteModelAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug, obj.name = obj.generate_unique_slug_and_name(slugify(obj.name), obj.name)
        try:
            super().save_model(request, obj, form, change)
        except IntegrityError:
            self.message_user(request, f"Slug '{obj.slug}' already exists. Please try a different name.", level=messages.ERROR)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Category, CategoryAdmin)

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Comment, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Category model.
    It ustomizes the admin interface for the Category model by
    specifying the fields to display in the list view, and automatically
    generating the slug field based on the name field.
    Attributes:
        list_display (tuple): Fields to display
        in the list view of the admin interface.
        prepopulated_fields (dict): Fields to prepopulate
        based on other fields.
    """
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Post model.
    It ustomizes the admin interface for the Post model by
    specifying the fields to display in the list view, the fields to
    search, the filters to apply, and the fields to use the Summernote
    editor.
    Attributes:
        list_display (tuple): Fields to display in the list
        view of the admin interface.
        search_fields (list): Fields to include in the search functionality.
        list_filter (tuple): Fields to filter the list view by.
        prepopulated_fields (dict): Fields to prepopulate
        based on other fields.
        summernote_fields (tuple): Fields to use the Summernote editor.
    """
    list_display = ('title', 'category', 'status', 'created_on', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'updated_on', 'category')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Comment model.
    This class customizes the admin interface for the Comment model by
    specifying the fields to display in the list view, the filters to apply,
    and the search fields. It also adds an action to approve comments.
    Attributes:
        list_display (tuple): Fields to display in the
        list view of the admin interface.
        list_filter (tuple): Fields to filter the list view by.
        search_fields (tuple): Fields to include in the search functionality.
        actions (list): List of actions available in the admin interface.
    """

    list_display = ('user', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('user__username', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Custom admin action to approve comments.
        Args:
            request: The HTTP request object.
            queryset: The queryset of comments to be approved.
        Returns:
            None
        """
        queryset.update(approved=True)

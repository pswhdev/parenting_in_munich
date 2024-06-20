from django.contrib import admin
from .models import Link, Topic


# allows to add and edit Link objects directly within the Topic admin page
class LinkInline(admin.TabularInline):
    """
    Inline admin configuration for Link model.
    Allows adding and editing Link objects directly
    within the Topic admin page.
    Attributes:
        model (Model): The model class to be used for the inline.
        extra (int): The number of extra forms to display in the inline form.
        ordering (list): The fields to order the inline form by.
    """
    model = Link
    extra = 1
    # Order links by title alphabetically in the inline form
    ordering = ['title']


class TopicAdmin(admin.ModelAdmin):
    """
    Admin configuration for Topic model.
    Configures the admin interface for the Topic model, including inline Link
    objects, search fields, and ordering.
    Attributes:
        inlines (list): The inline classes to include in the admin interface.
        search_fields (tuple): The fields to include in
        the search functionality.
        ordering (list): The fields to order the list view by.
    """
    inlines = [LinkInline]
    # Adding search fields for autocomplete
    search_fields = ('name',)
    # Order topics by name alphabetically in the admin interface
    ordering = ['name']


class LinkAdmin(admin.ModelAdmin):
    """
    Admin configuration for Link model.
    Configures the admin interface for the Link model, including list display,
    search fields, list filters, autocomplete fields, and ordering.
    Attributes:
        list_display (tuple): The fields to display in the list view.
        search_fields (tuple): The fields to include in the
        search functionality.
        list_filter (tuple): The fields to filter the list view by.
        autocomplete_fields (list): The fields to autocomplete.
        ordering (list): The fields to order the list view by.
    """
    list_display = ('title', 'url', 'topic')
    search_fields = ('title', 'url')
    list_filter = ('topic',)
    # To autocomplete for topic field
    autocomplete_fields = ['topic']
    # Order links by title alphabetically in the admin interface
    ordering = ['title']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Link, LinkAdmin)

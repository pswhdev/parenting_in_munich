from django.contrib import admin
from .models import Link, Topic


# allows to add and edit Link objects directly within the Topic admin page
class LinkInline(admin.TabularInline):
    model = Link
    extra = 1
    # Order links by title alphabetically in the inline form
    ordering = ['title']


class TopicAdmin(admin.ModelAdmin):
    inlines = [LinkInline]
    # Adding search fields for autocomplete
    search_fields = ('name',)
    # Order topics by name alphabetically in the admin interface
    ordering = ['name']


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'topic')
    search_fields = ('title', 'url')
    list_filter = ('topic',)
    # To autocomplete for topic field
    autocomplete_fields = ['topic']
    # Order links by title alphabetically in the admin interface
    ordering = ['title']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Link, LinkAdmin)

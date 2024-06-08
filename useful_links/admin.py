from django.contrib import admin
from .models import Topic, Link

class LinkInline(admin.TabularInline):
    model = Link
    extra = 1

class TopicAdmin(admin.ModelAdmin):
    inlines = [LinkInline]
    # Adding search fields for autocomplete
    search_fields = ('name',)

class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'topic')
    search_fields = ('title', 'url')
    list_filter = ('topic',)
    # To autocomplete for topic field
    autocomplete_fields = ['topic']

admin.site.register(Topic, TopicAdmin)
admin.site.register(Link, LinkAdmin)

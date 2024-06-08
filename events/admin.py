from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin


class EventAdmin(SummernoteModelAdmin):
    list_display = ('name', 'location', 'date', 'time', 'image')
    search_fields = ('name', 'location')
    list_filter = ('date', 'location')
    summernote_fields = ('description',)

admin.site.register(Event, EventAdmin)

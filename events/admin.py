from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin
from django.core.exceptions import ValidationError


class EventAdmin(SummernoteModelAdmin):
    list_display = ('name', 'location', 'date', 'time', 'image')
    search_fields = ('name', 'location')
    list_filter = ('date', 'location')
    summernote_fields = ('description',)

    def save_model(self, request, obj, form, change):
        if not change:  # Only check for duplicates when adding a new record
            if Event.objects.filter(name=obj.name, description=obj.description, location=obj.location, time=obj.time, date=obj.date).exists():
                raise ValidationError('An event with this combination of details already exists.')
        super().save_model(request, obj, form, change)


admin.site.register(Event, EventAdmin)

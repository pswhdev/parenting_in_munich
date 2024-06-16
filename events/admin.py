from django.contrib import admin
from .models import Event
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
from django.core.exceptions import ValidationError


class EventAdmin(SummernoteModelAdmin):
    list_display = (
        "name",
        "location",
        "start_date",
        "end_date",
        "start_time",
        "end_time",
        "website_link",
    )
    search_fields = ("name", "location")
    list_filter = ("start_date", "end_date", "location")
    summernote_fields = ("description",)

    def website_link(self, obj):
        # Check if the website field is populated
        if obj.website:
            # Return a formatted HTML anchor tag that opens the link in a new
            # tab. The 2 {} are replaced by the obj.website.
            return format_html(
                '<a href="{}" target="_blank">{}</a>', obj.website, obj.website
            )
        # If the website field is empty or null,
        # return a hyphen as a placeholder
        return "-"

    # Set the header text for the column in the admin list view to 'Website'
    website_link.short_description = "Website"

    def save_model(self, request, obj, form, change):
        # Only check for duplicates when adding a new record
        if not change:
            if Event.objects.filter(
                name=obj.name,
                description=obj.description,
                location=obj.location,
                start_date=obj.start_date,
                end_date=obj.end_date,
            ).exists():
                raise ValidationError(
                    "An event with this combination of details already exists."
                )
        super().save_model(request, obj, form, change)


admin.site.register(Event, EventAdmin)

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
from .models import Event


class EventAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Event model.
    **List Display:**
        - name: The name of the event.
        - location: The location of the event.
        - start_date: The start date of the event.
        - end_date: The end date of the event.
        - formatted_time: The formatted start and end time of the event.
        - website_link: The website link for the event.
    **Search Fields:**
        - name
        - location
    **List Filter:**
        - start_date
        - end_date
        - location
    **Summernote Fields:**
        - description
    """
    list_display = (
        "name",
        "location",
        "start_date",
        "end_date",
        "formatted_time",
        "website_link",
    )
    search_fields = ("name", "location")
    list_filter = ("start_date", "end_date", "location")
    summernote_fields = ("description",)

    def website_link(self, obj):
        """
        Display the website link as a clickable URL in the admin list view.
        If the website field is populated, returns a formatted HTML anchor tag
        that opens the link in a new tab. If the website field is empty o
        null, returns a hyphen as a placeholder.
        **Args:**
            obj: The Event instance.
        **Returns:**
            str: HTML for the website link or a hyphen.
        """

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

    def formatted_time(self, obj):
        """
        Display the formatted start and end time for the event.
        If the end time is specified, returns a string with the format
        "start_time - end_time".
        Otherwise, returns a string with the format "from start_time".
        Args:
            obj: The Event instance.
        Returns:
            str: The formatted time string.
        """

        if obj.end_time:
            return f"{obj.start_time} - {obj.end_time}"
        return f"from {obj.start_time}"

    formatted_time.short_description = "Time"

    def save_model(self, request, obj, form, change):
        """
        Save the Event model instance, ensuring no duplicate events.
        Only checks for duplicates when adding a new record.
        If an event with the same combination of name, description,
        location, start date, and end date already exists,
        raises a ValidationError.
        **Args:**
            request: The HTTP request object.
            obj: The Event instance being saved.
            form: The form instance used to create or update the object.
            change: A boolean indicating whether the object is being
            changed or added.
        **Raises:**
            ValidationError: If a duplicate event is detected.
        """

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

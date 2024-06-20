from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, ContactUs


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin configuration for About model.
    This class uses SummernoteModelAdmin to allow rich text editing for the
    'content' field in the About model.
    Attributes:
        summernote_fields (tuple): Fields that will use the Summernote editor.
    """
    summernote_fields = ('content',)


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """
    Admin configuration for ContactUs model.
    This class customizes the admin interface for the ContactUs model by
    specifying which fields to display in the list view.
    Attributes:
        list_display (tuple): Fields to display in the list view of the admin
        interface.
    """
    list_display = ('message', 'read',)

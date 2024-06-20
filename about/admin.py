from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, ContactUs


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin configuration for About model.
    """
    summernote_fields = ('content',)


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """
    Admin configuration for ContactUs model.
    """
    list_display = ('message', 'read',)

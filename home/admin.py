from django.contrib import admin
from .models import HeroSection
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(HeroSection)
class HeroSectionAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('text',)

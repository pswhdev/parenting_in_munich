from .models import ContactUs
from django import forms
from django.core.exceptions import ValidationError


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message')

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message.strip() == '':
            raise ValidationError(
                'Message cannot be blank or contain only whitespace.'
                )
        return message

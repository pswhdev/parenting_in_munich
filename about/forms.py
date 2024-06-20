from django import forms
from django.core.exceptions import ValidationError
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    """
    A form for contacting the website administrators.
    Allows users to provide their name, email, and message.
    It includes validation for the message field to
    ensure it is not blank or contains only whitespace.
    """

    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'message')

    def clean_message(self):
        """
        Validates the message field by chicking if the message
        field is blank or contains only whitespace.
        If the message is invalid, raises a ValidationError.
        """
        message = self.cleaned_data.get('message')
        if message.strip() == '':
            raise ValidationError(
                'This field is required.'
            )
        return message

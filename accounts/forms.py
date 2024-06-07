from django import forms
from django.contrib.auth.models import User
from .models import Profile, MUNICH_DISTRICTS


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    location = forms.ChoiceField(choices=MUNICH_DISTRICTS)
    custom_location = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['photo', 'location', 'custom_location', 'bio']

    def clean(self):
        cleaned_data = super().clean()
        location = cleaned_data.get('location')
        custom_location = cleaned_data.get('custom_location')

        if location == 'Others' and not custom_location:
            self.add_error('custom_location', 'Custom location is'
                           'required when Others is selected.')
        return cleaned_data

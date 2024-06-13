from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from allauth.account.forms import LoginForm
from .models import Profile, MUNICH_DISTRICTS


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["email"]


class ProfileUpdateForm(forms.ModelForm):
    location = forms.ChoiceField(choices=[("Others", "Others")] + MUNICH_DISTRICTS)
    custom_location = forms.CharField(required=False)
    display_email = forms.BooleanField(required=False)

    class Meta:
        model = Profile
        fields = [
            "photo",
            "full_name",
            "display_email",
            "bio",
            "location",
            "custom_location",
        ]

    def clean(self):
        cleaned_data = super().clean()
        location = cleaned_data.get("location")
        custom_location = cleaned_data.get("custom_location")

        if location == "Others" and not custom_location:
            self.add_error(
                "custom_location",
                "Custom location is required when Others is selected.",
            )
        return cleaned_data


class CustomLoginForm(LoginForm):
    def clean(self):
        User = get_user_model()
        username = self.cleaned_data.get('login')
        password = self.cleaned_data.get('password')

        if username and not User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "The username doesn't exist. Please check "
                "or sign up to create an account."
            )

        return super().clean()

import io
from PIL import Image
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile, UploadedFile
from allauth.account.forms import LoginForm
from .models import MUNICH_DISTRICTS, Profile


class UserUpdateForm(forms.ModelForm):
    """
    A form for updating user information.
    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["email"]


class ProfileUpdateForm(forms.ModelForm):
    """
    A form for updating profile information.
    """

    location = forms.ChoiceField(
        choices=[("Others", "Others")] + MUNICH_DISTRICTS
    )
    custom_location = forms.CharField(required=False)
    display_email = forms.BooleanField(required=False)
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'maxlength': 500}),
        required=False
    )

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

    def clean_photo(self):
        photo = self.cleaned_data.get("photo")

        if photo and isinstance(photo, UploadedFile):
            # Check file size
            if photo.size > 2 * 1024 * 1024:
                raise forms.ValidationError("File size must be less than 2MB")

            # Validate and convert image format
            try:
                image = Image.open(photo)
                if image.format.lower() != "webp":
                    # Convert to WebP
                    output = io.BytesIO()
                    image.save(output, format="webp")
                    output.seek(0)
                    # Replace the uploaded file with the converted file
                    photo = InMemoryUploadedFile(
                        output,
                        "ImageField",
                        f"{photo.name.split('.')[0]}.webp",
                        "image/webp",
                        output.tell(),
                        None,
                    )
                    self.cleaned_data["photo"] = photo
            except IOError:
                raise forms.ValidationError("Invalid image file")

        return photo

    def clean(self):
        cleaned_data = super().clean()
        location = cleaned_data.get("location")
        custom_location = cleaned_data.get("custom_location")

        return cleaned_data


class CustomLoginForm(LoginForm):
    """
    Checks if the provided username exists in the User model
    to give the user a feedback if the username doesn't exist.
    """

    def clean(self):
        User = get_user_model()
        username = self.cleaned_data.get("login")
        password = self.cleaned_data.get("password")

        if username and not User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "The username doesn't exist. Please check "
                "or sign up to create an account."
            )

        return super().clean()

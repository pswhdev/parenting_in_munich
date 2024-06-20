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
    Attributes:
        email (EmailField): The user's email address.
    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["email"]


class ProfileUpdateForm(forms.ModelForm):
    """
    A form for updating profile information.
    Attributes:
        location (ChoiceField): The user's location, chosen from
        predefined choices or custom.
        custom_location (CharField): A custom location if 'Others' is selected.
        display_email (BooleanField): Whether to display the
        user's email publicly.
        bio (CharField): A short biography of the user.
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
        """
        Validate and convert the uploaded photo to WebP format.
        Raises:
            forms.ValidationError: If the file size is greater than
            2MB or if the file is not a valid image.
        Returns:
            InMemoryUploadedFile: The validated
            and converted photo.
        """
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
        """
        Perform custom validation for the form.
        Ensures that if a custom location is specified, the location
        field is set appropriately.
        Returns:
            dict: The cleaned data.
        """
        cleaned_data = super().clean()
        location = cleaned_data.get("location")
        custom_location = cleaned_data.get("custom_location")

        return cleaned_data


class CustomLoginForm(LoginForm):
    """
    Custom login form to provide feedback if the username does not exist.
    Attributes:
        None
    Methods:
        clean: Validates the login form by checking if the provided
        username exists in the User model.
    """

    def clean(self):
        """
        Validate the login form.
        Checks if the provided username exists in the User model to give
        feedback if the username doesn't exist.
        Raises:
            forms.ValidationError: If the username doesn't exist.
        Returns:
            dict: The cleaned data.
        """
        User = get_user_model()
        username = self.cleaned_data.get("login")
        password = self.cleaned_data.get("password")

        if username and not User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "The username doesn't exist. Please check "
                "or sign up to create an account."
            )

        return super().clean()

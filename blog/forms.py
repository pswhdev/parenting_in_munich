from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from allauth.account.forms import SignupForm
from .models import Comment, UsedUsername


class CommentForm(forms.ModelForm):
    """
    Form for submitting comments.
    Includes a content field for the comment,
    with a maximum length of 1000 characters.
    Validates that the content is not blank or whitespace.
    Attributes:
        content (CharField): The content of the comment.
    """
    content = forms.CharField(
        widget=forms.Textarea(attrs={'maxlength': 1000}),
        required=True
    )

    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        """
        Validate the content field.
        Ensure that the content is not blank or whitespace.
        **Returns:**
            str: The cleaned content.
        **Raises:**
            ValidationError: If the content is blank or whitespace.
        """
        content = self.cleaned_data.get('content')
        if content.strip() == '':
            raise ValidationError(
                'This field is required.'
            )
        return content


# To customize the signing up
class CustomSignupForm(SignupForm):
    """
    Custom form for user signup.
    This form includes an additional field for accepting site rules and
    validates that the username has not been previously used.
    Attributes:
        accept_rules (BooleanField): Field for accepting site rules.
    """
    accept_rules = forms.BooleanField(
        # User needs to accept policy before signing up
        label=mark_safe(
            'I accept the <a href="/site-rules/"'
            ' target="_blank">site rules</a>'
        ),
        required=True
    )

    def clean_username(self):
        """
        Validate the username field.
        Ensure that the username has not been previously used.
        **Returns:**
            str: The cleaned username.
        **Raises:**
            ValidationError: If the username has been previously used.
        """
        username = self.cleaned_data.get('username')

        # Check if the username is already in use by another user
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                f"The username '{username}' is already in use."
            )

        # Check if the username has been previously used
        if UsedUsername.objects.filter(username=username).exists():
            raise forms.ValidationError(
                f"The username '{username}' has been "
                "used previously and cannot be reused."
            )

        return username

    def save(self, request):
        """
        Save the form.
        Saves the user instance and performs any additional processing.
        Args:
            request: The HTTP request object.
        Returns:
            User: The saved user instance.
        """
        user = super(CustomSignupForm, self).save(request)
        return user

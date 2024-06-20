from django import forms
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from allauth.account.forms import SignupForm
from .models import Comment, UsedUsername


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'maxlength': 1000}),
        required=True
    )

    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if content.strip() == '':
            raise ValidationError(
                'Comment cannot be blank or contain only whitespace.'
                )
        return content


# To customize the signing up
class CustomSignupForm(SignupForm):
    # User needs to accept policy before signing up
    accept_rules = forms.BooleanField(
        label=mark_safe(
            'I accept the <a href="/site-rules/"'
            ' target="_blank">site rules</a>'
            ),
        required=True
    )

    # Usernames cannot be reused even if the account has been deleted
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if UsedUsername.objects.filter(username=username).exists():
            raise forms.ValidationError(
                f"The username '{username}' has been "
                "used previously and cannot be reused."
            )
        return username

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user

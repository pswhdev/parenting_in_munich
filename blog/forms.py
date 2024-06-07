from .models import Comment
from django import forms
from allauth.account.forms import SignupForm
from .models import UsedUsername


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class CustomSignupForm(SignupForm):
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if UsedUsername.objects.filter(username=username).exists():
            raise forms.ValidationError(
                f"The username '{username}' "
                "has been used previously and cannot be reused."
                )
        return username

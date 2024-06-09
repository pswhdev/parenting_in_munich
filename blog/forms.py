from django import forms
from .models import Comment
from .models import UsedUsername
from allauth.account.forms import SignupForm
from django.utils.safestring import mark_safe


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class CustomSignupForm(SignupForm):
    accept_rules = forms.BooleanField(
        label=mark_safe(
            'I accept the <a href="/site-rules/"'
            ' target="_blank">site rules</a>'
            ),
        required=True
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if UsedUsername.objects.filter(username=username).exists():
            raise forms.ValidationError(
                f"The username '{username}' has been used previously and cannot be reused."
            )
        return username

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user

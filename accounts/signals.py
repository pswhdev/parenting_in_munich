from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(user_signed_up, sender=User)
def create_profile_on_signup(request, user, **kwargs):
    Profile.objects.create(user=user)

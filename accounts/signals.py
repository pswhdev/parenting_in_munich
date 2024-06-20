from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from .models import Profile


# Creates a profile when a user signs up via allauth
@receiver(user_signed_up, sender=User)
def create_profile_on_signup(request, user, **kwargs):
    Profile.objects.get_or_create(user=user)


# Creates a profile when a new User instance is saved
# using django for create superusers for instance
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

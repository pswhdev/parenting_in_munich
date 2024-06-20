from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from .models import Profile


# Creates a profile when a user signs up via allauth
@receiver(user_signed_up, sender=User)
def create_profile_on_signup(request, user, **kwargs):
    """
    Create a profile when a user signs up via allauth.
    This signal handler creates a Profile instance for the user when they sign
    up through the allauth package.
    Args:
        request: The HTTP request object.
        user: The User instance that has signed up.
        **kwargs: Additional keyword arguments.
    """
    Profile.objects.get_or_create(user=user)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Create a profile when a new User instance is saved.
    This signal handler creates a Profile instance for the user when a new
    User instance is created, such as when creating superusers via Django.
    Args:
        sender: The model class (User).
        instance: The instance of the model that was saved.
        created: A boolean indicating whether the instance was created.
        **kwargs: Additional keyword arguments.
    """
    if created:
        Profile.objects.get_or_create(user=instance)

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile


class Command(BaseCommand):
    """
    A Django management command to create profiles for users
    who do not have one.
    This command checks all users in the database and creates
    a profile for each user who does not currently have a profile
    associated with their account.
    Attributes:
        help (str): Description of the command for the help message.
    """
    help = "Create profiles for users who do not have one"

    def handle(self, *args, **kwargs):
        """
        This method queries the database for users without profiles,
        creates a profile for each of them, and outputs a success message
        for each profile created.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        users_without_profiles = User.objects.filter(profile__isnull=True)
        for user in users_without_profiles:
            Profile.objects.create(user=user)
            self.stdout.write(
                self.style.SUCCESS(
                    "Profile created for " f"user {user.username}"
                )
            )

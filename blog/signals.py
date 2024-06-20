from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Post, Comment, UsedUsername


@receiver(pre_delete, sender=User)
def update_author_before_user_delete(sender, instance, **kwargs):
    """
    Signal handler to update the author field before deleting a user.
    Ensures the integrity of the database by updating the
    author field of related Post and Comment instances to a deactivated
    username format before the user is deleted. It also saves the user's
    username in the UsedUsername model to prevent reuse.
    Args:
        sender: The model class (User).
        instance: The instance of the model that is being deleted.
        **kwargs: Additional keyword arguments.
    """
    deactivated_username = f"{instance.username} [Deactivated]"

    # Save the username to UsedUsername
    UsedUsername.objects.get_or_create(username=instance.username)

    # Update Post author field
    posts = Post.objects.filter(user=instance)
    for post in posts:
        post.author = deactivated_username
        post.save()

    # Update Comment author field
    comments = Comment.objects.filter(user=instance)
    for comment in comments:
        comment.author = deactivated_username
        comment.save()


@receiver(pre_save, sender=User)
def prevent_reused_usernames(sender, instance, **kwargs):
    """
    Signal handler to prevent the reuse of usernames.
    Checks if the username being saved has been previously
    used and raises a ValueError if it has. This ensures that usernames
    cannot be reused once they have been associated with an account.
    Args:
        sender: The model class (User).
        instance: The instance of the model that is being saved.
        **kwargs: Additional keyword arguments.
    Raises:
        ValueError: If the username has been used previously.
    """
    if UsedUsername.objects.filter(username=instance.username).exists():
        raise ValueError(
            f"The username '{instance.username}' "
            "has been used previously and cannot be reused."
        )

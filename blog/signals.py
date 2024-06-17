from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Post, Comment, UsedUsername


# Signal to update the author field before deleting the user
# in order to keep the integrity of the database
@receiver(pre_delete, sender=User)
def update_author_before_user_delete(sender, instance, **kwargs):
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


# Signal to prevent reuse of usernames
@receiver(pre_save, sender=User)
def prevent_reused_usernames(sender, instance, **kwargs):
    if UsedUsername.objects.filter(username=instance.username).exists():
        raise ValueError(
            f"The username '{instance.username}' "
            "has been used previously and cannot be reused."
            )

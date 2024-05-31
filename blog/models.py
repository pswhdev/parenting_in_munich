from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS = (
        (0, 'Draft'),
        (1, 'Published')
        )
    
    # To allow the post to remain on the database and the site
    # even if the user is deleted
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="blog_posts")
    author = models.CharField(max_length=150, null=True, blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    def save(self, *args, **kwargs):
        if self.user and not self.author:
            self.author = self.user.username
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} | written by {self.author}"

    class Meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='commenter')
    author = models.CharField(max_length=150, null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.user and not self.author:
            self.author = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
    
    class Meta:
        ordering = ["created_on"]


# Signal to update the author field before deleting the user
# in order to keep the integrity of the database
@receiver(pre_delete, sender=User)
def update_author_before_user_delete(sender, instance, **kwargs):
    deactivated_username = f"{instance.username} [Deactivated]"
    
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



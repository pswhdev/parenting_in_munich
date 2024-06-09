from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug, self.name = self.generate_unique_slug_and_name(slugify(self.name), self.name)
        super().save(*args, **kwargs)

    def generate_unique_slug_and_name(self, slug, name):
        unique_slug = slug
        unique_name = name
        num = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            unique_name = f'{name} {num}'
            num += 1
        return unique_slug, unique_name

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS = ((0, "Draft"), (1, "Published"))

    # To allow the post to remain on the database and the site
    # even if the user is deleted
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="blog_posts"
    )
    author = models.CharField(max_length=150, null=True, blank=True)
    featured_image = CloudinaryField("image", default="placeholder")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # To make sure the author has the username so if the user account
    # is deleted the name is still saved on the system
    def save(self, *args, **kwargs):
        if self.user and not self.author:
            self.author = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    class Meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="comments_author"
    )
    author = models.CharField(max_length=150, null=True, blank=True)
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    # To make sure the author has the username so if the user account
    # is deleted the name is still saved on the system
    def save(self, *args, **kwargs):
        if self.user and not self.author:
            self.author = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Comment {self.content} by {self.author}"

    class Meta:
        ordering = ["created_on"]


# To keep track of usernames used on the website (used by the signal)
class UsedUsername(models.Model):
    username = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.username

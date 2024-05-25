from django.db import models
from django.contrib.auth.models import User

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
    
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="blog_posts")
    author = models.CharField(max_length=150, null=True, blank=True)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    excerpt = models.TextField(blank=True)
    
    # To override the save method to set the username field
    # so that if a user is deleted we can still see who wrote it
    def save(self, *args, **kwargs):
        if self.user and not self.author:
            self.author = self.user.username
        # Call the superclass's save method to save the object to the DB
        super().save(*args, **kwargs)    

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    class Meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='commenter')
    author = models.CharField(max_length=150, null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.user and not self.author:
            self.author = self.user.username
        # Call the superclass's save method to save the object to the DB
        super().save(*args, **kwargs) 

    def __str__(self):

        return f"Comment by {self.author} on {self.post.title}"
    
    class Meta:
        ordering = ["created_on"]
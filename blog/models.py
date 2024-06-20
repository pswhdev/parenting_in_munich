from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Represents a category for blog posts.
    Attributes:
        name (str): Name of the category.
        slug (str): Slugified version of the category name, used in URLs.
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
        max_length=100, unique=True, blank=True
    )

    def save(self, *args, **kwargs):
        """
        Override the save method to auto-generate the slug if not provided.
        """
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # Allows to perform custom validation on the
    # model instance before it is saved.
    def clean(self):
        """
        Perform custom validation to avoid duplicate categories.
        Raises:
            ValidationError: If a category with the same name already exists.
        """
        if Category.objects.filter(
            name=self.name
        ).exclude(id=self.id).exists():
            raise ValidationError(
                f"The category with name '{self.name}' already exists."
            )

    def __str__(self):
        """Return a string representation of the category."""
        return self.name


class Post(models.Model):
    """
    Represents a blog post.

    Attributes:
        title (str): Title of the post.
        slug (str): Slugified version of the post title, used in URLs.
        user (User): User who created the post.
        author (str): Name of the post author.
        featured_image (CloudinaryField): Featured image for the post.
        content (str): Content of the post.
        created_on (datetime): Date and time when the post was created.
        status (int): Status of the post (draft or published).
        excerpt (str): A short excerpt of the post.
        updated_on (datetime): Date and time when the post was last updated.
        category (Category): Category to which the post belongs.
    """
    STATUS = ((0, "Draft"), (1, "Published"))

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # To allow the post to remain on the database and the site
    # even if the user is deleted
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        related_name="blog_posts"
    )
    author = models.CharField(max_length=150, null=True, blank=True)
    featured_image = CloudinaryField("image", default="placeholder")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, related_name="posts",
        on_delete=models.CASCADE
    )

    # To make sure the author has the username so if the user account
    # is deleted the name is still saved on the system
    def save(self, *args, **kwargs):
        """Override the save method to set the author if not provided."""

        if self.user and not self.author:
            self.author = self.user.username
        super().save(*args, **kwargs)

    # Allows to perform custom validation on the model
    # instance before it is saved.
    def clean(self):
        """
        Perform custom validation to avoid duplicate post titles.
        Raises:
            ValidationError: If a post with the same title already exists.
        """
        if Post.objects.filter(title=self.title).exclude(id=self.id).exists():
            raise ValidationError(
                f"A post with the title '{self.title}' already exists."
            )

    def __str__(self):
        """Return a string representation of the post."""
        return f"{self.title} | written by {self.author}"

    class Meta:
        ordering = ["-updated_on"]


class Comment(models.Model):
    """
    Represents a comment on a blog post.
    Attributes:
        post (Post): Post to which the comment belongs.
        user (User): User who created the comment.
        author (str): Name of the comment author.
        content (str): Content of the comment.
        approved (bool): Indicates whether the comment is approved.
        created_on (datetime): Date and time when the comment was created.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
        )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        related_name="comments_author"
    )
    author = models.CharField(max_length=150, null=True, blank=True)
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    # To make sure the author has the username so if the user account
    # is deleted the name is still saved on the system
    def save(self, *args, **kwargs):
        """Override the save method to set the author if not provided."""
        if self.user and not self.author:
            self.author = self.user.username
        super().save(*args, **kwargs)

    def __str__(self):
        """Return a string representation of the comment."""
        return f"Comment {self.content} by {self.author}"

    class Meta:
        ordering = ["created_on"]


# To keep track of usernames used on the website (used by the signal)
class UsedUsername(models.Model):
    """
    Represents a previously used username.
    Attributes:
        username (str): The previously used username.
    """
    username = models.CharField(max_length=150, unique=True)

    def __str__(self):
        """Return a string representation of the used username."""
        return self.username

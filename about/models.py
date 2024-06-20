from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Represents the About section of the website.
    Attributes:
        title (str): The title of the About section.
        profile_image (CloudinaryField): Profile image for the About section.
        updated_on (datetime): Date and time the About was last updated.
        content (str): The content of the About section.
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        """Return a string representation of the About instance."""
        return self.title


class ContactUs(models.Model):
    """
    Represents a contact message from a user.
    Attributes:
        name (str): The name of the person sending the message.
        email (str): The email address of the person sending the message.
        message (str): The content of the message.
        read (bool): Indicates whether the message has been read.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        """Return a string representation of the ContactUs instance."""
        return f"Message from {self.name}"

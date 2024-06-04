from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class HeroSection(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')
    text = models.TextField()

    def __str__(self):
        return "Hero Section"

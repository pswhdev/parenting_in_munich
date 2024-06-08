from django.db import models
from cloudinary.models import CloudinaryField


DEFAULT_IMAGE_URL=(
    "https://res.cloudinary.com/daluxpssk/image/"
    "upload/v1717835739/placeholderimage_ujh6em.svg"
)


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    image = CloudinaryField("image", default=DEFAULT_IMAGE_URL)

    def __str__(self):
        return self.name

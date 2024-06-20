import datetime
from django.db import models
from cloudinary.models import CloudinaryField


DEFAULT_IMAGE_URL = (
    "https://res.cloudinary.com/daluxpssk/image/"
    "upload/v1717835739/placeholderimage_ujh6em.svg"
)


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    # Default start time at 9 AM
    start_time = models.TimeField(default=datetime.time(9, 0))
    # Optional end time
    end_time = models.TimeField(blank=True, null=True)
    image = CloudinaryField("image", default=DEFAULT_IMAGE_URL)
    website = models.URLField(blank=True, null=True)

    class Meta:
        unique_together = (
            "name",
            "description",
            "location",
            "start_date",
            "end_date")

    def __str__(self):
        return self.name

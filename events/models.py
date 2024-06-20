import datetime
from django.db import models
from cloudinary.models import CloudinaryField


DEFAULT_IMAGE_URL = (
    "https://res.cloudinary.com/daluxpssk/image/"
    "upload/v1717835739/placeholderimage_ujh6em.svg"
)


class Event(models.Model):
    """
    Represents an event.
    Attributes:
        name (str): The name of the event.
        description (str): A detailed description of the event.
        location (str): The location where the event will be held.
        start_date (date): The start date of the event.
        end_date (date): The end date of the event.
        start_time (time): The start time of the event (default: 9:00 AM).
        end_time (time, optional): The end time of the event.
        image (CloudinaryField): An image associated with the event.
        website (URLField, optional): A URL for the event's website.
    """
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
        """
        Return a string representation of the event.
        """
        return self.name

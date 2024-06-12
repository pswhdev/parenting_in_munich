from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

MUNICH_DISTRICTS = [
    ("Allach", "Allach"),
    ("Altstadt-Lehel", "Altstadt-Lehel"),
    ("Aubing", "Aubing"),
    ("Au-Haidhausen", "Au-Haidhausen"),
    ("Berg am Laim", "Berg am Laim"),
    ("Bogenhausen", "Bogenhausen"),
    ("Fasangarten", "Fasangarten"),
    ("Feldmoching-Hasenbergl", "Feldmoching-Hasenbergl"),
    ("Forstenried", "Forstenried"),
    ("Freimann", "Freimann"),
    ("Fürstenried", "Fürstenried"),
    ("Hadern", "Hadern"),
    ("Harlaching", "Harlaching"),
    ("Laim", "Laim"),
    ("Langwied", "Langwied"),
    ("Lochhausen", "Lochhausen"),
    ("Ludwigsvorstadt-Isarvorstadt", "Ludwigsvorstadt-Isarvorstadt"),
    ("Maxvorstadt", "Maxvorstadt"),
    ("Milbertshofen-Am Hart", "Milbertshofen-Am Hart"),
    ("Moosach", "Moosach"),
    ("Neuhausen", "Neuhausen"),
    ("Nymphenburg", "Nymphenburg"),
    ("Obersendling", "Obersendling"),
    ("Obergiesing", "Obergiesing"),
    ("Pasing", "Pasing"),
    ("Perlach", "Perlach"),
    ("Ramersdorf", "Ramersdorf"),
    ("Riem", "Riem"),
    ("Schwabing", "Schwabing"),
    ("Schwabing-West", "Schwabing-West"),
    ("Schwanthalerhöhe", "Schwanthalerhöhe"),
    ("Sendling", "Sendling"),
    ("Sendling-Westpark", "Sendling-Westpark"),
    ("Solln", "Solln"),
    ("Thalkirchen", "Thalkirchen"),
    ("Trudering", "Trudering"),
    ("Untergiesing", "Untergiesing"),
    ("Others", "Others"),
]

DEFAULT_IMAGE_URL = (
    "https://res.cloudinary.com/daluxpssk/image/upload"
    "/v1717744760/nobody_jm5djw.jpg"
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = CloudinaryField(
        "image", blank=True, null=True, default=DEFAULT_IMAGE_URL
        )
    location = models.CharField(
        max_length=100, choices=MUNICH_DISTRICTS, default="Others"
    )
    bio = models.TextField(blank=True, null=True)
    custom_location = models.CharField(max_length=100, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    display_email = models.BooleanField(default=False)  # New field to control email visibility

    def __str__(self):
        return f"{self.user.username} Profile"

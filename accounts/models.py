from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

MUNICH_DISTRICTS = [
    ('Altstadt-Lehel', 'Altstadt-Lehel'),
    ('Ludwigsvorstadt-Isarvorstadt', 'Ludwigsvorstadt-Isarvorstadt'),
    ('Maxvorstadt', 'Maxvorstadt'),
    ('Schwabing-West', 'Schwabing-West'),
    ('Au-Haidhausen', 'Au-Haidhausen'),
    ('Sendling', 'Sendling'),
    ('Sendling-Westpark', 'Sendling-Westpark'),
    ('Schwanthalerhöhe', 'Schwanthalerhöhe'),
    ('Neuhausen-Nymphenburg', 'Neuhausen-Nymphenburg'),
    ('Moosach', 'Moosach'),
    ('Milbertshofen-Am Hart', 'Milbertshofen-Am Hart'),
    ('Schwabing-Freimann', 'Schwabing-Freimann'),
    ('Bogenhausen', 'Bogenhausen'),
    ('Berg am Laim', 'Berg am Laim'),
    ('Trudering-Riem', 'Trudering-Riem'),
    ('Ramersdorf-Perlach', 'Ramersdorf-Perlach'),
    ('Obergiesing-Fasangarten', 'Obergiesing-Fasangarten'),
    ('Untergiesing-Harlaching', 'Untergiesing-Harlaching'),
    ('Thalkirchen-Obersendling-Forstenried-Fürstenried-Solln', 'Thalkirchen-Obersendling-Forstenried-Fürstenried-Solln'),
    ('Hadern', 'Hadern'),
    ('Pasing-Obermenzing', 'Pasing-Obermenzing'),
    ('Aubing-Lochhausen-Langwied', 'Aubing-Lochhausen-Langwied'),
    ('Allach-Untermenzing', 'Allach-Untermenzing'),
    ('Feldmoching-Hasenbergl', 'Feldmoching-Hasenbergl'),
    ('Laim', 'Laim'),
    ('Others', 'Others'),
]

DEFAULT_IMAGE_URL = 'https://res.cloudinary.com/daluxpssk/image/upload/v1717744760/nobody_jm5djw.jpg'


class Profile(models.Model):
    user = models.One-to-OneField(User, on_delete=models.CASCADE)
    photo = CloudinaryField('image', blank=True, null=True, default=DEFAULT_IMAGE_URL)
    location = models.CharField(max_length=100, choices=MUNICH_DISTRICTS, default='Others')
    bio = models.TextField(blank=True, null=True)
    custom_location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

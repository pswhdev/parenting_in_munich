from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    # To order topics alphabetically by name on the useful_links page
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Link(models.Model):
    topic = models.ForeignKey(
        Topic, related_name='links', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200, unique=True)
    url = models.URLField(unique=True)

    # To order links alphabetically by title on the useful_links page
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

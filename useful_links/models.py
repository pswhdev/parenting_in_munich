from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Link(models.Model):
    topic = models.ForeignKey(
        Topic, related_name='links', on_delete=models.CASCADE
        )
    title = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title

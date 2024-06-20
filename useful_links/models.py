from django.db import models


class Topic(models.Model):
    """
    Represents a topic for categorizing links.
    Attributes:
        name (str): The name of the topic.
    """
    name = models.CharField(max_length=100, unique=True)

    # To order topics alphabetically by name on the useful_links page
    class Meta:
        ordering = ['name']

    def __str__(self):
        """
        Return a string representation of the topic.
        """
        return self.name


class Link(models.Model):
    """
    Represents a link associated with a topic.
    Attributes:
        topic (Topic): The topic to which the link is related.
        title (str): The title of the link.
        url (str): The URL of the link.
    """
    topic = models.ForeignKey(
        Topic, related_name='links', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200, unique=True)
    url = models.URLField(unique=True)

    # To order links alphabetically by title on the useful_links page
    class Meta:
        ordering = ['title']

    def __str__(self):
        """
        Return a string representation of the link.
        """
        return self.title

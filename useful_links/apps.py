from django.apps import AppConfig


class UsefulLinksConfig(AppConfig):
    """
    Configuration class for the Useful Links app.
    Attributes:
        default_auto_field (str): Specifies the type of auto
        field to use for primary keys.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'useful_links'

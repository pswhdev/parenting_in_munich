from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Configuration class for the About app.
    Sets the default auto field type and the name of the app.
    Attributes:
        default_auto_field (str): Type of auto field to use for primary keys.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configuration class for the Blog app.
    Sets the default auto field type and the name of the app.
    It also imports the signals module when the app is ready.
    Attributes:
        default_auto_field (str): The type of auto field to
        use for primary keys.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        """Import the signals module when the app is ready."""
        import blog.signals

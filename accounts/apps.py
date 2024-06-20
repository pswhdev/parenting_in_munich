from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    AppConfig for the 'accounts' app.
    Attributes:
        default_auto_field (str): Specifies the type of auto
        field to use for primary keys.
        name (str): The name of the app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        """
        Import the signals module to ensure that the signals are registered
        when the app is ready.
        """
        import accounts.signals

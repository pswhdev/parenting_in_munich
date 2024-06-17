from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    AppConfig for the 'accounts' app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # Importing signals module to ensure that the
        # signals are registered when the app is ready.
        import accounts.signals

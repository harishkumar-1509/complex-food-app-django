from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    
    # for signal implementation (Importing the signals file in the accounts app)
    def ready(self):
        import accounts.signals

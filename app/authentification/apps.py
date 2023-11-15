"""apps module contains AppConfig"""

from django.apps import AppConfig


class AuthentificationConfig(AppConfig):
    """handle authentifaction config settings

    Args:
        AppConfig (Any): django application config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentification'

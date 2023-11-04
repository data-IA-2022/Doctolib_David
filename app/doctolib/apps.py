"""Apps module"""
from django.apps import AppConfig


class DoctolibConfig(AppConfig):
    """
    Args:
        AppConfig (class): django config class
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'doctolib'

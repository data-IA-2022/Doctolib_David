"""Admin Module for authentification"""

from django.contrib import admin
from authentification.models import Utilisateur, MedecinPatient


admin.site.register(Utilisateur)
admin.site.register(MedecinPatient)
# Register your models here.

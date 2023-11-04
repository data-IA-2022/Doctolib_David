"""Contains Models
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class Utilisateur(AbstractUser):
    """User Class that inherite from AbstractUser

    Args:
        AbstractUser (class): django AbstractUser class
    """
    ROLE_CHOICES = (
          ('doctor', 'Doctor'),
          ('patient', 'Patient'),
      )
    role = models.CharField(choices=ROLE_CHOICES,
                            blank=True,
                            null=True,
                            max_length=10)


class MedecinPatient(models.Model):
    """Class for the medecinModel table

    Args:
        models (class): django Model class
    """
    idPatient = models.ForeignKey(Utilisateur,
                                  null=True,
                                  on_delete=models.CASCADE,
                                  related_name='patientMedecin',
                                  unique=True)
    idMedecin = models.ForeignKey(Utilisateur,
                                  null=True,
                                  on_delete=models.CASCADE,
                                  related_name='medecinPatient')
# class Connexion(models.Model):
#     username = models.CharField(max_length=50)
#     motDePasse = models.CharField(max_length=50)

# Create your models here.

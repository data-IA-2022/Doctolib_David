from django.core.management.base import BaseCommand
from faker import Faker
from authentification.models import Utilisateur


class Command(BaseCommand):
    help = 'Command Information'

    def handle(self, *args, **kwargs):
        fake = Faker()
        # fake.add_provider(Provider)
        for _ in range(20):
            username = fake.unique.first_name()
            email = fake.unique.email()
            pwd = fake.unique.password()
            role = 'patient'
            Utilisateur.objects.create(
                username=username,
                email=email,
                password=pwd,
                role=role)
        for _ in range(5):
            username = fake.unique.first_name()
            email = fake.unique.email()
            pwd = fake.unique.password()
            role = 'doctor'
            Utilisateur.objects.create(
                username=username,
                email=email,
                password=pwd,
                role=role)

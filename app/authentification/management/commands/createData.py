from django.core.management.base import BaseCommand
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
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
            fake_pwd = BaseUserManager().make_random_password(12)
            pwd = make_password(fake_pwd)
            role = 'patient'
            Utilisateur.objects.create(
                username=username,
                email=email,
                password=pwd,
                role=role)
            with open('mdp.txt', 'a', encoding='utf-8') as f:
                f.write(f'{username}, {role}: {fake_pwd}\n')
        for _ in range(5):
            username = fake.unique.first_name()
            email = fake.unique.email()
            fake_pwd = BaseUserManager().make_random_password(12)
            pwd = make_password(fake_pwd)
            role = 'doctor'
            Utilisateur.objects.create(
                username=username,
                email=email,
                password=pwd,
                role=role)
            with open('mdp.txt', 'a', encoding='utf-8') as f:
                f.write(f'{username}, {role}: {fake_pwd}\n')

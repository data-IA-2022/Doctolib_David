from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers import python
from numpy import random
from authentification.models import Utilisateur
from doctolib.models import General_form_record
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Command Information'

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(python)
        names = Utilisateur.objects.filter(role='patient')
        print(len(names))
        for name in names:
            for idx in range(5):
                date = datetime.now() + timedelta(days=30*idx)
                patient_username = name.username  # This field type is a guess.
                created_at = date
                poids = random.uniform(40, 120)
                taille_cm = random.uniform(140, 200)
                frequence_cardiaque = random.randint(50, 100)
                tension_arterielle = random.randint(60, 140)
                description_symptomes_cardio = random.choice(
                    ['Aucun', 'Légers', 'Modérés', 'Graves'])
                nombres_medicaments = random.randint(0, 10)
                oublie_prise_medicaments = random.choice(['Non', 'Oui'])
                presence_effets_secondaire = random.choice(['Non', 'Oui'])
                symptomes_particulier = random.choice(['Non', 'Oui'])
                description_effets_symptomes = random.choice(
                    ['N/A', 'Douleurs', 'Maux de tête', 'Nausées'])
                consommation_alcool = random.choice(
                    ['Aucune', 'Occasionnelle', 'Fréquente'])
                grignotage = random.choice(
                    ['Aucun', 'Occasionnel', 'Fréquent'])
                repas_pris_journee_field = random.randint(1, 5)
                quantite_eau_litre = round(random.uniform(0.5, 3.0), 2)
                quantite_alcool_litre = round(random.uniform(0, 2.0), 2)
                activite_physique_jour = random.choice(
                    ['Aucune', 'Légère', 'Modérée', 'Intense'])
                duree_activite = random.randint(15, 120)

                General_form_record.objects.create(
                    patient_username=patient_username,
                    created_at=created_at,
                    poids=poids,
                    taille_cm=taille_cm,
                    frequence_cardiaque=frequence_cardiaque,
                    tension_arterielle=tension_arterielle,
                    description_symptomes_cardio=description_symptomes_cardio,
                    nombres_medicaments=nombres_medicaments,
                    oublie_prise_medicaments=oublie_prise_medicaments,
                    presence_effets_secondaire=presence_effets_secondaire,
                    symptomes_particulier=symptomes_particulier,
                    description_effets_symptomes=description_effets_symptomes,
                    consommation_alcool=consommation_alcool,
                    grignotage=grignotage,
                    repas_pris_journee_field=repas_pris_journee_field,
                    quantite_eau_litre=quantite_eau_litre,
                    quantite_alcool_litre=quantite_alcool_litre,
                    activite_physique_jour=activite_physique_jour,
                    duree_activite=duree_activite,
                    )

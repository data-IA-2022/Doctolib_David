"""Module to create fake user"""

from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers import python
import numpy as np
from authentification.models import Utilisateur
from doctolib.models import StressFormRecord


class Command(BaseCommand):
    """Commmand class """
    help = 'Command Information'

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(python)
        names = Utilisateur.objects.filter(role='patient')
        print(len(names))
        for name in names:
            for idx in range(5):
                date = datetime.now() + timedelta(days=30*idx)
                patient_username = name.username
                created_at = date
                dyspnee = np.random.choice(['Non', 'Oui'])
                oedeme = np.random.choice(['Non', 'Oui'])
                episodes_infectieux = np.random.choice(['Non', 'Oui'])
                fievre = np.random.choice(['Non', 'Oui'])
                palpitation = np.random.choice(['Non', 'Oui'])
                douleur_thoracique = np.random.choice(['Non', 'Oui'])
                malaise = np.random.choice(['Non', 'Oui'])
                valeurs_natremie = np.random.uniform(100, 200)
                valeurs_potassium = np.random.uniform(2.5, 6.5)
                taux_fer_serique = np.random.randint(50, 180)
                taux_hemoglobine = np.random.randint(120, 180)
                taux_proteine_c_reactive = np.random.randint(5, 12)
                taux_vitamine_d = np.random.randint(20, 60)
                taux_acide_urique = np.random.randint(150, 420)
                taux_inr = np.random.randint(1, 6)
                irritabilite = np.random.choice([0, 1, 5, 10])
                bouche_seche_gorge_seche = np.random.choice([0, 1, 5, 10])
                actions_gestes_impulsifs = np.random.choice([0, 1, 5, 10])
                difficulte_rester_assis = np.random.choice([0, 1, 5, 10])
                cauchermars = np.random.choice([0, 1, 5, 10])
                diarrhee = np.random.choice([0, 1, 5, 10])
                hauts_bas_emotifs = np.random.choice([0, 1, 5, 10])
                fatigue_lourdeur_general = np.random.choice([0, 1, 5, 10])
                sentiment_anxiete = np.random.choice([0, 1, 5, 10])
                tension_emotionnelle = np.random.choice([0, 1, 5, 10])
                hostilite_vers_autres = np.random.choice([0, 1, 5, 10])
                tremblements_gestes_nerveux = np.random.choice([0, 1, 5, 10])
                begaiements_hesitations_verbales = np.random.choice(
                    [0, 1, 5, 10])
                incapacite_difficulte_concentrer = np.random.choice(
                    [0, 1, 5, 10])
                difficulte_dormir_nuit_sans_reveiller = np.random.choice(
                    [0, 1, 5, 10])
                besoin_frequent_uriner = np.random.choice([0, 1, 5, 10])
                maux_estomac_difficultes_digerer = np.random.choice(
                    [0, 1, 5, 10])
                maux_tete = np.random.choice([0, 1, 5, 10])
                douleurs_dos_nuque = np.random.choice([0, 1, 5, 10])
                perte_gain_appetit = np.random.choice([0, 1, 5, 10])
                perte_interet_sexe = np.random.choice([0, 1, 5, 10])
                oublis_frequents = np.random.choice([0, 1, 5, 10])
                douleurs_serrements_poitrine = np.random.choice([0, 1, 5, 10])
                difficultes_lever_apres_sommeil = np.random.choice(
                    [0, 1, 5, 10])
                difficulte_longue_activite_continue = np.random.choice(
                    [0, 1, 5, 10])
                difficulte_s_endormir = np.random.choice([0, 1, 5, 10])
                difficulte_se_remettre_evenement_contrariant = \
                    np.random.choice([0, 1, 5, 10])
                mains_moites = np.random.choice([0, 1, 5, 10])
                impact_stress_vie_actuelle = sum([
                    irritabilite,
                    bouche_seche_gorge_seche,
                    actions_gestes_impulsifs,
                    difficulte_rester_assis,
                    cauchermars,
                    diarrhee,
                    hauts_bas_emotifs,
                    fatigue_lourdeur_general,
                    sentiment_anxiete,
                    tension_emotionnelle,
                    hostilite_vers_autres,
                    tremblements_gestes_nerveux,
                    begaiements_hesitations_verbales,
                    incapacite_difficulte_concentrer,
                    difficulte_dormir_nuit_sans_reveiller,
                    besoin_frequent_uriner,
                    maux_estomac_difficultes_digerer,
                    maux_tete,
                    douleurs_dos_nuque,
                    perte_gain_appetit,
                    perte_interet_sexe,
                    oublis_frequents,
                    douleurs_serrements_poitrine,
                    difficultes_lever_apres_sommeil,
                    difficulte_longue_activite_continue,
                    difficulte_s_endormir,
                    difficulte_se_remettre_evenement_contrariant,
                    mains_moites,
                ])

                StressFormRecord.objects.create(
                    patient_username=patient_username,
                    created_at=created_at,
                    dyspnee=dyspnee,
                    oedeme=oedeme,
                    episodes_infectieux=episodes_infectieux,
                    fievre=fievre,
                    palpitation=palpitation,
                    douleur_thoracique=douleur_thoracique,
                    malaise=malaise,
                    valeurs_natremie=valeurs_natremie,
                    valeurs_potassium=valeurs_potassium,
                    taux_fer_serique=taux_fer_serique,
                    taux_hemoglobine=taux_hemoglobine,
                    taux_proteine_c_reactive=taux_proteine_c_reactive,
                    taux_vitamine_d=taux_vitamine_d,
                    taux_acide_urique=taux_acide_urique,
                    taux_inr=taux_inr,
                    irritabilite=irritabilite,
                    bouche_seche_gorge_seche=bouche_seche_gorge_seche,
                    actions_gestes_impulsifs=actions_gestes_impulsifs,
                    difficulte_rester_assis=difficulte_rester_assis,
                    cauchermars=cauchermars,
                    diarrhee=diarrhee,
                    hauts_bas_emotifs=hauts_bas_emotifs,
                    fatigue_lourdeur_generalisees=fatigue_lourdeur_general,
                    sentiment_anxiete=sentiment_anxiete,
                    tension_emotionnelle=tension_emotionnelle,
                    hostilite_vers_autres=hostilite_vers_autres,
                    tremblements_gestes_nerveux=tremblements_gestes_nerveux,
                    begaiements_hesitations_verbales=begaiements_hesitations_verbales,
                    incapacite_difficulte_concentrer=incapacite_difficulte_concentrer,
                    difficulte_dormir_nuit_sans_reveiller=difficulte_dormir_nuit_sans_reveiller,
                    besoin_frequent_uriner=besoin_frequent_uriner,
                    maux_estomac_difficultes_digerer=maux_estomac_difficultes_digerer,
                    maux_tete=maux_tete,
                    douleurs_dos_nuque=douleurs_dos_nuque,
                    perte_gain_appetit=perte_gain_appetit,
                    perte_interet_sexe=perte_interet_sexe,
                    oublis_frequents=oublis_frequents,
                    douleurs_serrements_poitrine=douleurs_serrements_poitrine,
                    difficultes_lever_apres_sommeil=difficultes_lever_apres_sommeil,
                    difficulte_longue_activite_continue=difficulte_longue_activite_continue,
                    difficulte_s_endormir=difficulte_s_endormir,
                    difficulte_se_remettre_evenement_contrariant=difficulte_se_remettre_evenement_contrariant,
                    mains_moites=mains_moites,
                    impact_stress_vie_actuelle=impact_stress_vie_actuelle,
                )

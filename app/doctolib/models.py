"""Models module for doctolib"""

from datetime import date
from django.db import models
from django.views.generic.list import ListView
from authentification.models import Utilisateur, MedecinPatient


class GeneralFormRecord(models.Model):
    """class for table schema

    Args:
        models (class): django models
    """
    patient_username = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateField(default=date.today())
    poids_kg = models.BigIntegerField(blank=True, null=True)
    taille_cm = models.BigIntegerField(blank=True, null=True)
    frequence_cardiaque = models.BigIntegerField(blank=True, null=True)
    tension_arterielle = models.BigIntegerField(blank=True, null=True)
    description_symptomes_cardio = models.TextField(blank=True, null=True)
    nombres_medicaments = models.BigIntegerField(blank=True, null=True)
    oublie_prise_medicaments = models.TextField(blank=True, null=True)
    presence_effets_secondaire = models.TextField(blank=True, null=True)
    symptomes_particulier = models.TextField(blank=True, null=True)
    description_effets_symptomes = models.TextField(blank=True, null=True)
    consommation_alcool = models.TextField(blank=True, null=True)
    grignotage = models.TextField(blank=True, null=True)
    repas_pris_journee_field = models.BigIntegerField(
        db_column='repas_pris_journee ',
        blank=True,
        null=True)
    quantite_eau_litre = models.TextField(blank=True, null=True)
    quantite_alcool_litre = models.TextField(blank=True, null=True)
    activite_physique_jour = models.TextField(blank=True, null=True)
    description_activite = models.TextField(blank=True, null=True)
    duree_activite = models.BigIntegerField(blank=True, null=True)


class StressFormRecord(models.Model):
    """Model for the stress form table

    Args:
        models (models.Model): base django model
    """

    patient_username = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateField(default=date.today())
    dyspnee = models.TextField(blank=True, null=True)
    oedeme = models.TextField(blank=True, null=True)
    episodes_infectieux = models.TextField(blank=True, null=True)
    fievre = models.TextField(blank=True, null=True)
    palpitation = models.TextField(blank=True, null=True)
    douleur_thoracique = models.TextField(blank=True, null=True)
    malaise = models.TextField(blank=True, null=True)
    valeurs_natremie = models.TextField(blank=True, null=True)  # This field type is a guess.
    valeurs_potassium = models.TextField(blank=True, null=True)  # This field type is a guess.
    taux_fer_serique = models.BigIntegerField(blank=True, null=True)
    taux_hemoglobine = models.BigIntegerField(blank=True, null=True)
    taux_proteine_c_reactive = models.BigIntegerField(blank=True, null=True)
    taux_vitamine_d = models.BigIntegerField(blank=True, null=True)
    taux_acide_urique = models.BigIntegerField(blank=True, null=True)
    taux_inr = models.BigIntegerField(blank=True, null=True)
    irritabilite = models.BigIntegerField(blank=True, null=True)
    bouche_seche_gorge_seche = models.BigIntegerField(blank=True, null=True)
    actions_gestes_impulsifs = models.BigIntegerField(blank=True, null=True)
    difficulte_rester_assis = models.BigIntegerField(blank=True, null=True)
    cauchermars = models.BigIntegerField(blank=True, null=True)
    diarrhee = models.BigIntegerField(blank=True, null=True)
    hauts_bas_emotifs = models.BigIntegerField(blank=True, null=True)
    fatigue_lourdeur_generalisees = models.BigIntegerField(blank=True, null=True)
    sentiment_anxiete = models.BigIntegerField(blank=True, null=True)
    tension_emotionnelle = models.BigIntegerField(blank=True, null=True)
    hostilite_vers_autres = models.BigIntegerField(blank=True, null=True)
    tremblements_gestes_nerveux = models.BigIntegerField(blank=True, null=True)
    begaiements_hesitations_verbales = models.BigIntegerField(blank=True, null=True)
    incapacite_difficulte_concentrer = models.BigIntegerField(blank=True, null=True)
    difficulte_dormir_nuit_sans_reveiller = models.BigIntegerField(blank=True, null=True)
    besoin_frequent_uriner = models.BigIntegerField(blank=True, null=True)
    maux_estomac_difficultes_digerer = models.BigIntegerField(blank=True, null=True)
    maux_tete = models.BigIntegerField(blank=True, null=True)
    douleurs_dos_nuque = models.BigIntegerField(blank=True, null=True)
    perte_gain_appetit = models.BigIntegerField(blank=True, null=True)
    perte_interet_sexe = models.BigIntegerField(blank=True, null=True)
    oublis_frequents = models.BigIntegerField(blank=True, null=True)
    douleurs_serrements_poitrine = models.BigIntegerField(blank=True, null=True)
    difficultes_lever_apres_sommeil = models.BigIntegerField(blank=True, null=True)
    difficulte_longue_activite_continue = models.BigIntegerField(blank=True, null=True)
    difficulte_s_endormir = models.BigIntegerField(blank=True, null=True)
    difficulte_se_remettre_evenement_contrariant = models.BigIntegerField(blank=True, null=True)
    mains_moites = models.BigIntegerField(blank=True, null=True)
    impact_stress_vie_actuelle = models.BigIntegerField(blank=True, null=True)


class GeneralFormList(ListView):
    """_summary_

    Args:
        ListView (class): django class

    """
    model = GeneralFormRecord
    template_name = 'general_form_record_list.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['field_names'] = [field.name for field in GeneralFormRecord._meta.fields]
        username = self.request.user.username
        print(self.request.user.username)
        if self.request.user.is_superuser:
            context['records'] = GeneralFormRecord.objects.values(*context['field_names'])
            return context
        if self.request.user.role == 'patient':
            context['records'] = GeneralFormRecord.objects.filter(patient_username=username).values(*context['field_names'])
            return context
        idx = Utilisateur.objects.filter(username=username)[0]
        list_patients = [v.idPatient.username for v in MedecinPatient.objects.filter(idMedecin=idx)]
        print(list_patients)
        context['records'] = GeneralFormRecord.objects.filter(patient_username__in=list_patients).values(*context['field_names'])
        return context


class StressFormList(ListView):
    """Class for display list 

    Args:
        ListView (class): django ListView class

    """
    model = StressFormRecord
    template_name = 'stress_form_record_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.user.username
        context['field_names'] = [field.name for field in StressFormRecord._meta.fields]
        if self.request.user.is_superuser:
            context['records'] = StressFormRecord.objects.values(*context['field_names'])
            return context
        if self.request.user.role == 'patient':
            context['records'] = StressFormRecord.objects.filter(patient_username=username).values(*context['field_names'])
            return context
        idx = Utilisateur.objects.filter(username=username)[0]
        list_patients = [v.idPatient.username for v in MedecinPatient.objects.filter(idMedecin=idx)]
        print(list_patients)
        context['records'] = StressFormRecord.objects.filter(patient_username__in=list_patients).values(*context['field_names'])
        return context

"""doctolib views modules"""

from datetime import timedelta, date
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
import pandas as pd
from authentification.models import Utilisateur, MedecinPatient
from doctolib.models import GeneralFormRecord, StressFormRecord
from doctolib.forms import PostGeneralForm, PostStressForm


@login_required
def home(request):
    """handle client request in th home page

    Args:
        request (Any): request object

    Returns:
        Any: render object
    """
    return render(request, 'index.html')


@login_required
def comptes(request):
    """handle account creation

    Args:
        request (Any): request object

    Returns:
        Any: handle render modif on the page
    """
    regex_mdp = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+-]).{8,}$"
    message = ""
    if request.method == "POST":
        ancien_mdp = request.POST["ancien_mdp"]
        new_mdp1 = request.POST["new_mdp1"]
        new_mdp2 = request.POST["new_mdp2"]

        verification = authenticate(username=request.user.username,
                                    password=ancien_mdp)
        if verification is not None:
            if new_mdp1 == new_mdp2:
                utilisateur = Utilisateur.objects.get(
                    username=request.user.username)
                # utilisateur = Utilisateur.objects.get(id=request.user.id)
                utilisateur.set_password(request.POST.get("new_mdp1"))
                utilisateur.save()
                return redirect("accueil")
            message = "⚠️ Les deux mot de passe ne concordent pas ⚠️"
        else:
            message = "L'ancien mot de passe n'est pas bon. T'es qui toi ? 😡"
    return render(request,
                  "comptes.html",
                  {"regex_mdp": regex_mdp, "message": message})


@login_required
def eda(request):
    """View for the eda page

    Args:
        request (Any): request object

    Returns:
        Any: render the result on the page
    """
    # if request.user.role != "doctor":
    # return redirect("home")
    # else:
    values = GeneralFormRecord.objects.all()
    names = [value.patient_username for value in values]
    freqs = [value.frequence_cardiaque for value in values]
    df = pd.DataFrame({
        'names': names,
        'freqence': freqs,
    })
    df_gr = df.groupby('names').mean().reset_index()
    labels = list(df_gr[df_gr.columns.values[0]])
    data = list(df_gr[df_gr.columns.values[1]])

    stress_values = StressFormRecord.objects.all()
    names = [v.patient_username for v in stress_values]
    stress_impact = [v.impact_stress_vie_actuelle for v in stress_values]

    df_stress = pd.DataFrame({
        'names': names,
        'freqence': stress_impact,
    })

    df_grstr = df_stress.groupby('names').mean().reset_index()
    stress_labels = list(df_grstr[df_grstr.columns.values[0]])
    stress_data = list(df_grstr[df_grstr.columns.values[1]])
    return render(request, "eda.html", {
            'labels': labels,
            'data': data,
            'stress_labels': stress_labels,
            'stress_data': stress_data,
        })


@login_required
def attribution(request):
    """View for the attribution feature

    Args:
        request (Any ): request object

    Returns:
        Any: render the result on the page
    """
    # 1- Récupérer la liste des id des médecins et des patients
    # 2- Ensuite on ne garde que les patients qui ne sont pas dans
    # la table medecinPatient
    # 3- On créé ensuite un template qui contiendra une liste déroulante
    # 4- Dans cette liste déroulante on va afficher d'un côté les médecins
    # et de l'autre les patients filtrés (voir étapge 2)
    # https://developer.mozilla.org/fr/docs/Web/HTML/Element/select
    medecins_id = \
        [medecin.username for medecin in Utilisateur.objects.filter(
            role="doctor")]
    patients_id = \
        [patient.username for patient in Utilisateur.objects.filter(
            role="patient")]
    list_patients_associes = \
        [ligne.idPatient for ligne in MedecinPatient.objects.all()]
    list_patients_non_associes = \
        [id for id in patients_id if id not in list_patients_associes]
    table_association_medecin_patient = MedecinPatient.objects.all()
    # Syntaxte équivalente
    # for id in patients_id :
    #    if id not in list_patients_associes:
    #        patientsNonAssocies.append(id)


    if request.method == "POST":
        medecin = request.POST["medecin"]
        patient = request.POST["patient"]
        MedecinPatient(idMedecin=Utilisateur.objects.filter(
                       username=medecin)[0],
                       idPatient=Utilisateur.objects.filter(
                       username=patient)[0]).save()
        # MedecinPatient.save()
        return redirect('attribution')
    return render(request, "attribution.html", {
        "list_patients_non_associes": list_patients_non_associes,
        "medecins_id": medecins_id,
        "table_association_medecin_patient": table_association_medecin_patient})


@login_required
def historique(request):
    """View for the historique page

    Args:
        request (Any): request from the client

    Returns:
        Any: render the result
    """
    username = request.user.username
    print(username)
    table_association_medecin_patient = MedecinPatient.objects.all()
    if request.user.is_superuser:
        return render(request, 'historique.html',
                    {"table_association_medecin_patient": table_association_medecin_patient})

    idx = Utilisateur.objects.filter(username=username)[0]
    table_patients = [v.idPatient.username for v in MedecinPatient.objects.filter(idMedecin=idx)]
    print(table_patients)
    return render(request, 'historique.html',
                  {'table_patients': table_patients})


@login_required
def post_general_form(request):
    """Handle post request

    Args:
        request (Any): request from the client

    Returns:
        Any: render the result on the page
    """
    username = request.user.username
    user_id = Utilisateur.objects.filter(username=username)[0]
    period_general_form = user_id.period_general_from
    print(period_general_form)
    query_date = GeneralFormRecord.objects.filter(patient_username=username)
    if not query_date:
        if request.method == "POST":
            formulaire = PostGeneralForm(request.POST)
            if formulaire.is_valid():
                formulaire.save()
        else:
            formulaire = PostGeneralForm()
        return render(request,
                    "general_form.html",
                    {"formulaire": formulaire})
        
    last_date = sorted([v.created_at for v in query_date])[-1]
    print(last_date)
    current_date = last_date - date.today()
    print(current_date < timedelta(days=1))
    if current_date > timedelta(days=1):
        if request.method == "POST":
            formulaire = PostGeneralForm(request.POST)
            if formulaire.is_valid():
                formulaire.save()
        else:
            formulaire = PostGeneralForm()
        return render(request,
                    "general_form.html",
                    {"formulaire": formulaire})
    
    message = f'Formulaire à déjà été rempli, vous devez attendre {current_date - timedelta(days=1)}'
    return render(request, 'general_form.html', {"message": message})


@login_required
def post_stress_form(request):
    """Handle post request

    Args:
        request (Any): request from the client

    Returns:
        Any: render the result on the page
    """
    username = request.user.username
    user_id = Utilisateur.objects.filter(username=username)[0]
    period_general_form = user_id.period_general_from
    print(period_general_form)
    query_date = GeneralFormRecord.objects.filter(patient_username=username)
    if not query_date:
        if request.method == "POST":
            formulaire = PostGeneralForm(request.POST)
            if formulaire.is_valid():
                formulaire.save()
        else:
            formulaire = PostGeneralForm()
        return render(request,
                    "general_form.html",
                    {"formulaire": formulaire})
        
    last_date = sorted([v.created_at for v in query_date])[-1]
    print(last_date)
    current_date = last_date - date.today()
    print(current_date < timedelta(days=1))
    if current_date > timedelta(days=1):
        if request.method == "POST":
            formulaire = PostGeneralForm(request.POST)
            if formulaire.is_valid():
                formulaire.save()
        else:
            formulaire = PostGeneralForm()
        return render(request,
                    "general_form.html",
                    {"formulaire": formulaire})

    message = f'Formulaire à déjà été rempli, vous devez attendre {current_date - timedelta(days=5)}'
    return render(request, 'general_form.html', {"message": message})

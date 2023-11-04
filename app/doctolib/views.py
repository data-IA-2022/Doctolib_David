from django.shortcuts import render, redirect
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from authentification.models import Utilisateur, MedecinPatient
from doctolib.models import General_form_record, Stress_form_record
from doctolib.forms import PostGeneralForm, PostStressForm


@login_required
def home(request):
    return render(request, 'index.html')


@login_required
def comptes(request):
    regexMDP = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+-]).{8,}$"
    message = ""
    if request.method == "POST":
        ancienMDP = request.POST["ancienMDP"]
        nouveauMDP1 = request.POST["nouveauMDP1"]
        nouveauMDP2 = request.POST["nouveauMDP2"]

        verification = authenticate(username=request.user.username,
                                    password=ancienMDP)
        if verification is not None:
            if nouveauMDP1 == nouveauMDP2:
                utilisateur = Utilisateur.objects.get(
                    username=request.user.username)
                # utilisateur = Utilisateur.objects.get(id=request.user.id)
                utilisateur.set_password(request.POST.get("nouveauMDP1"))
                utilisateur.save()
                return redirect("accueil")
            else:
                message = "⚠️ Les deux mot de passe ne concordent pas ⚠️"
        else:
            message = "L'ancien mot de passe n'est pas bon. T'es qui toi ? 😡"
    return render(request,
                  "comptes.html",
                  {"regexMDP": regexMDP, "message": message})


@login_required
def eda(request):
    # if request.user.role != "doctor":
    # return redirect("home")
    # else:
    values = General_form_record.objects.all()
    names = [value.patient_username for value in values]
    freqs = [value.frequence_cardiaque for value in values]
    df = pd.DataFrame({
        'names': names,
        'freqence': freqs,
    })
    df_gr = df.groupby('names').mean().reset_index()
    labels = [v for v in df_gr[df_gr.columns.values[0]]]
    data = [v for v in df_gr[df_gr.columns.values[1]]]

    stress_values = Stress_form_record.objects.all()
    names = [v.patient_username for v in stress_values]
    stress_impact = [v.impact_stress_vie_actuelle for v in stress_values]

    df_stress = pd.DataFrame({
        'names': names,
        'freqence': stress_impact,
    })

    df_grstr = df_stress.groupby('names').mean().reset_index()
    stress_labels = [v for v in df_grstr[df_grstr.columns.values[0]]]
    stress_data = [v for v in df_grstr[df_grstr.columns.values[1]]]
    return render(request, "eda.html", {
            'labels': labels,
            'data': data,
            'stress_labels': stress_labels,
            'stress_data': stress_data,
        })


@login_required
def attribution(request):
    # 1- Récupérer la liste des id des médecins et des patients
    # 2- Ensuite on ne garde que les patients qui ne sont pas dans
    # la table medecinPatient
    # 3- On créé ensuite un template qui contiendra une liste déroulante
    # 4- Dans cette liste déroulante on va afficher d'un côté les médecins
    # et de l'autre les patients filtrés (voir étapge 2)
    # https://developer.mozilla.org/fr/docs/Web/HTML/Element/select
    medecinsID = \
        [medecin.username for medecin in Utilisateur.objects.filter(
            role="doctor")]
    patientsID = \
        [patient.username for patient in Utilisateur.objects.filter(
            role="patient")]
    listePatientsAssocies = \
        [ligne.idPatient for ligne in MedecinPatient.objects.all()]
    listePatientsNonAssocies = \
        [id for id in patientsID if id not in listePatientsAssocies]
    tableAssociationMedecinPatient = MedecinPatient.objects.all()
    # Syntaxte équivalente
    # for id in patientsID :
    #    if id not in listePatientsAssocies:
    #        patientsNonAssocies.append(id)

    if request.method == "POST":
        medecin = request.POST["medecin"]
        patient = request.POST["patient"]
        MedecinPatient(idMedecin=Utilisateur.objects.filter(
            username=medecin)[0],
                       idPatient=Utilisateur.objects.filter(
                           username=patient)[0]).save()
        # medecinPatient.save()
        return redirect('attribution')
    return render(request, "attribution.html", {
        "listePatientsNonAssocies": listePatientsNonAssocies,
        "medecinsID": medecinsID,
        "tableAssociationMedecinPatient": tableAssociationMedecinPatient})


@login_required
def post_general_form(request):
    if request.method == "POST":
        formulaire = PostGeneralForm(request.POST)
        if formulaire.is_valid():
            formulaire.save()
    else:
        formulaire = PostGeneralForm()
    return render(request,
                  "general_form.html",
                  {"formulaire": formulaire})


@login_required
def post_stress_form(request):
    if request.method == "POST":
        formulaire = PostStressForm(request.POST)
        if formulaire.is_valid():
            formulaire.save()
    else:
        formulaire = PostStressForm()
    return render(request,
                  "stress_form.html",
                  {"formulaire": formulaire})

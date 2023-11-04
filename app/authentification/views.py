"""This module contains django views
"""
import random
import string
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from authentification.models import Utilisateur


def connexion(request):
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        mdp = request.POST['mdp']
        verification = authenticate(username=username, password=mdp)
        print(username, mdp, verification)
        if verification is not None:
            login(request, verification)
            return redirect('comptes')
        else:
            message = 'username ou/et mot de passe incorrect'
    return render(request, 'connexion.html', {'message': message})
# Create your views here.


def deconnect(request):
    logout(request)
    return redirect('connexion')


def inscription(request):
    ideeMDP = "".join([
        random.choice(string.printable) for _ in range(12)]).replace(" ", "")
    if request.method == "POST":
        username = request.POST["username"]
        motDePasse = request.POST["motDePasse"]
        role = request.POST['role']
        print(role)
        _ = Utilisateur.objects.create_user(username=username,
                                            password=motDePasse,
                                            role=role)

        return redirect("connexion")

    return render(request,
                  "inscription.html",
                  {"ideeMDP": ideeMDP.replace(" ", "")})

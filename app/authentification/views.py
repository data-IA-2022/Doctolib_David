"""This module contains django views
"""
import random
import string
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from authentification.models import Utilisateur


def connexion(request):
    """View for the connexion feature

    Args:
        request (Any): request object received from the client  

    Returns:
        Any: render object 
    """
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
    """View for the deconnect feature

    Args:
        request (Any): request object

    Returns:
        Any: render function
    """
    logout(request)
    return redirect('connexion')


def inscription(request):
    """View for the incrisption feature

    Args:
        request (Any): request  object

    Returns:
        Any: render the result on the pages
    """
    idee_mdp = "".join([
        random.choice(string.printable) for _ in range(12)]).replace(" ", "")
    if request.method == "POST":
        username = request.POST["username"]
        mot_de_passe = request.POST["mot_de_passe"]
        role = request.POST['role']
        print(role)
        _ = Utilisateur.objects.create_user(username=username,
                                            password=mot_de_passe,
                                            role=role)

        return redirect("connexion")

    return render(request,
                  "inscription.html",
                  {"idee_mdp": idee_mdp.replace(" ", "")})

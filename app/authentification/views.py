from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

def connexion(request):
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        mdp = request.POST['mdp']
        verification = authenticate(username=username, password=mdp)
        if verification != None:
            login(request, verification)
            return redirect('home')
        else:
            message = 'username ou/et mot de passe incorrect'
    return render(request, 'connexion.html', {'message': message})
# Create your views here.

def deconnect(request):
    logout(request)
    return redirect('connexion')
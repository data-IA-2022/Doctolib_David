from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.template import loader

@login_required
def home(request):
  return render(request, 'index.html')

# Create your views here.

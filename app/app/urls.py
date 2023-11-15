"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from doctolib.views import (
    home,
    comptes,
    eda,
    historique,
    attribution,
    post_general_form,
    post_stress_form)
from doctolib.models import GeneralFormList, StressFormList
from authentification.views import connexion, deconnect, inscription

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', connexion, name='connexion'),
    path('deconnect', deconnect, name='deconnect'),
    path('inscription', inscription, name='inscription'),
    path('historique', historique, name='historique'),
    path('comptes', comptes, name='comptes'),
    path('eda', eda, name='eda'),
    path('attribution', attribution, name='attribution'),
    path('general_form', post_general_form, name='general_form'),
    path('stress_form', post_stress_form, name='stress_form'),
    path(
        'consultation/general',
        login_required(GeneralFormList.as_view()),
        name='consult_general'),
    path(
        'consultation/stress',
        login_required(StressFormList.as_view()),
        name='consult_stress'),
]

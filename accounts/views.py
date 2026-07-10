from django.shortcuts import render
from .models import Projet

def home(request):
    # On va chercher tous les projets dans la base de données
    mes_projets = Projet.objects.all()
    # On les envoie à une page HTML (qu'on va appeler home.html)
    return render(request, 'home.html', {'projets': mes_projets})from django.shortcuts import render

# Create your views here.

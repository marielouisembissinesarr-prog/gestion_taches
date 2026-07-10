from django.shortcuts import render
from .models import Projet

def home(request):
    mes_projets = Projet.objects.all()
    return render(request, 'home.html', {'projets': mes_projets})
# Create your views here.

from django.shortcuts import render
from .models import Tache  # <-- On importe Tache maintenant !

def home(request):
    # On récupère toutes les tâches de la base de données
    mes_taches = Tache.objects.all()
    return render(request, 'home.html', {'taches': mes_taches})
# Create your views here.

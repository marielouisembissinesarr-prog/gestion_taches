from django.shortcuts import render, redirect
from .forms import ProjetForm

def home(request):
    return render(request, 'home.html')

def create_project(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            # On associe automatiquement l'utilisateur connecté comme créateur du projet
            projet = form.save(commit=False)
            projet.createur = request.user
            projet.save()
            return redirect('home')
    else:
        form = ProjetForm()
    return render(request, 'projects/create_project.html', {'form': form})

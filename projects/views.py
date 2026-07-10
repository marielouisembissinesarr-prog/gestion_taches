from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjetForm

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            projet = form.save(commit=False)
            projet.createur = request.user
            projet.save()
            # On redirige vers la racine brute en attendant de configurer la page d'accueil
            return redirect('/')  
    else:
        form = ProjetForm()
    
    return render(request, 'projects/create_project.html', {'form': form})

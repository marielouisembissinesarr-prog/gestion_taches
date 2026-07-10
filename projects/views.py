from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjetForm

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            projet = form.save(commit=False)
            projet.createur = request.user  # Ici, request.user sera forcément un vrai utilisateur connecté
            projet.save()
            return redirect('home')  # Assure-toi que l'URL 'home' existe, sinon remplace temporairement par '/'
    else:
        form = ProjetForm()
    
    return render(request, 'projects/create_project.html', {'form': form})
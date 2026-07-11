from django.shortcuts import render, get_object_or_such, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Projet, Tache
from .forms import ProjetForm, TacheForm

@login_required
def dashboard(request):
    # Liste de tous les projets où l'utilisateur est créateur ou membre
    projets = Projet.objects.filter(createur=request.user) | Projet.objects.filter(membres=request.user)
    return render(request, 'projects/dashboard.html', {'projets': projets.distinct()})

@login_required
def projet_create(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            projet = form.save(commit=False)
            projet.createur = request.user
            projet.save()
            form.save_m2m() # Important pour sauvegarder les membres
            return redirect('dashboard')
    else:
        form = ProjetForm()
    return render(request, 'projects/projet_form.html', {'form': form, 'titre': "Créer un Projet"})

@login_required
def projet_detail(request, id):
    projet = get_object_or_404(Projet, id=id)
    taches = projet.taches.all()
    return render(request, 'projects/projet_detail.html', {'projet': projet, 'taches': taches})

@login_required
def projet_update(request, id):
    projet = get_object_or_404(Projet, id=id)
    if projet.createur != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('projet_detail', id=projet.id)
    else:
        form = ProjetForm(instance=projet)
    return render(request, 'projects/projet_form.html', {'form': form, 'titre': "Modifier le Projet"})

@login_required
def projet_delete(request, id):
    projet = get_object_or_404(Projet, id=id)
    if projet.createur != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        projet.delete()
        return redirect('dashboard')
    return render(request, 'projects/projet_confirm_delete.html', {'projet': projet})

@login_required
def tache_create(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            tache = form.save(commit=False)
            tache.projet = projet
            tache.save()
            return redirect('projet_detail', id=projet.id)
    else:
        form = TacheForm()
    return render(request, 'projects/tache_form.html', {'form': form, 'projet': projet, 'titre': "Créer une Tâche"})

@login_required
def tache_detail(request, id):
    tache = get_object_or_404(Tache, id=id)
    return render(request, 'projects/tache_detail.html', {'tache': tache})

@login_required
def tache_update(request, id):
    tache = get_object_or_404(Tache, id=id)
    if request.method == 'POST':
        form = TacheForm(request.POST, instance=tache)
        if form.is_valid():
            form.save()
            return redirect('projet_detail', id=tache.projet.id)
    else:
        form = TacheForm(instance=tache)
    return render(request, 'projects/tache_form.html', {'form': form, 'projet': tache.projet, 'titre': "Modifier la Tâche"})

@login_required
def tache_delete(request, id):
    tache = get_object_or_404(Tache, id=id)
    projet_id = tache.projet.id
    if request.method == 'POST':
        tache.delete()
        return redirect('projet_detail', id=projet_id)
    return render(request, 'projects/tache_confirm_delete.html', {'tache': tache})
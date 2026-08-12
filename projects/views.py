from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProjetForm, TacheForm
from .models import Projet, Tache


def user_has_project_access(user, projet):
  """Vérifie si l'utilisateur est le créateur ou un membre du projet."""
  return user == projet.createur or projet.membres.filter(id=user.id).exists()


@login_required
def dashboard(request):
  projets = (
      Projet.objects.filter(createur=request.user)
      | Projet.objects.filter(membres=request.user)
  ).distinct()
  return render(request, "projects/dashboard.html", {"projets": projets})


@login_required
def projet_create(request):
  if request.method == "POST":
    form = ProjetForm(request.POST)
    if form.is_valid():
      projet = form.save(commit=False)
      projet.createur = request.user
      projet.save()
      form.save_m2m()
      messages.success(
          request, f'🎉 Le projet "{projet.titre}" a été créé avec succès !'
      )
      return redirect("dashboard")
  else:
    form = ProjetForm()
  return render(
      request,
      "projects/projet_form.html",
      {"form": form, "titre": "Créer un Projet"},
  )


@login_required
def projet_detail(request, id):
  projet = get_object_or_404(Projet, id=id)
  if not user_has_project_access(request.user, projet):
    raise PermissionDenied
  taches = projet.taches.all()
  return render(
      request,
      "projects/projet_detail.html",
      {"projet": projet, "taches": taches},
  )


@login_required
def projet_update(request, id):
  projet = get_object_or_404(Projet, id=id)
  if projet.createur != request.user:
    raise PermissionDenied
  if request.method == "POST":
    form = ProjetForm(request.POST, instance=projet)
    if form.is_valid():
      form.save()
      messages.info(
          request, f'✏️ Le projet "{projet.titre}" a été mis à jour.'
      )
      return redirect("projet_detail", id=projet.id)
  else:
    form = ProjetForm(instance=projet)
  return render(
      request,
      "projects/projet_form.html",
      {"form": form, "titre": "Modifier le Projet"},
  )


@login_required
def projet_delete(request, id):
  projet = get_object_or_404(Projet, id=id)
  if projet.createur != request.user:
    raise PermissionDenied
  if request.method == "POST":
    titre = projet.titre
    projet.delete()
    messages.warning(request, f'🗑️ Le projet "{titre}" a été supprimé.')
    return redirect("dashboard")
  return render(
      request, "projects/projet_confirm_delete.html", {"projet": projet}
  )


@login_required
def tache_create(request, projet_id):
  projet = get_object_or_404(Projet, id=projet_id)
  if not user_has_project_access(request.user, projet):
    raise PermissionDenied

  if request.method == "POST":
    form = TacheForm(request.POST, projet=projet)  # 👈 projet transmis
    if form.is_valid():
      tache = form.save(commit=False)
      tache.projet = projet
      tache.save()
      messages.success(
          request, f'✅ Tâche "{tache.titre}" ajoutée au projet !'
      )
      return redirect("projet_detail", id=projet.id)
  else:
    form = TacheForm(projet=projet)  # 👈 projet transmis

  return render(
      request,
      "projects/tache_form.html",
      {"form": form, "projet": projet, "titre": "Créer une Tâche"},
  )


@login_required
def tache_detail(request, id):
  tache = get_object_or_404(Tache, id=id)
  if not user_has_project_access(request.user, tache.projet):
    raise PermissionDenied
  return render(request, "projects/tache_detail.html", {"tache": tache})


@login_required
def tache_update(request, id):
  tache = get_object_or_404(Tache, id=id)
  if not user_has_project_access(request.user, tache.projet):
    raise PermissionDenied

  if request.method == "POST":
    form = TacheForm(
        request.POST, instance=tache, projet=tache.projet
    )  # 👈 projet transmis
    if form.is_valid():
      form.save()
      messages.info(request, f'✏️ Tâche "{tache.titre}" modifiée avec succès.')
      return redirect("projet_detail", id=tache.projet.id)
  else:
    form = TacheForm(instance=tache, projet=tache.projet)  # 👈 projet transmis

  return render(
      request,
      "projects/tache_form.html",
      {"form": form, "projet": tache.projet, "titre": "Modifier la Tâche"},
  )


@login_required
def tache_delete(request, id):
  tache = get_object_or_404(Tache, id=id)
  projet_id = tache.projet.id
  if not user_has_project_access(request.user, tache.projet):
    raise PermissionDenied
  if request.method == "POST":
    titre = tache.titre
    tache.delete()
    messages.warning(request, f'🗑️ Tâche "{titre}" supprimée.')
    return redirect("projet_detail", id=projet_id)
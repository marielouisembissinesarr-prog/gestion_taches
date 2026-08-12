from django import forms
from django.contrib.auth.models import User
from .models import Projet, Tache


class ProjetForm(forms.ModelForm):

  class Meta:
    model = Projet
    fields = ['titre', 'description', 'membres']

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # Rendre la sélection de membres optionnelle pour autoriser les projets solo
    self.fields['membres'].required = False


class TacheForm(forms.ModelForm):

  class Meta:
    model = Tache
    fields = [
        'titre',
        'description',
        'statut',
        'priorite',
        'assigne_a',
        'date_echeance',
    ]
   widgets = {
    'date_echeance': forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'
    ),
}

  def __init__(self, *args, **kwargs):
    projet = kwargs.pop('projet', None)
    super().__init__(*args, **kwargs)

    # Si le projet est passé en paramètre, on restreint l'assignation au créateur + membres
    if projet:
      self.fields['assigne_a'].queryset = (
          User.objects.filter(id=projet.createur.id) | projet.membres.all()
      ).distinct()
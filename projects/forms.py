from django import forms
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
        fields = ['titre', 'description', 'statut', 'priorite', 'date_echeance']
        widgets = {
            'date_echeance': forms.DateInput(attrs={'type': 'date'}),
        }
from django import forms
from .models import Project  # Assure-toi que ton modèle s'appelle bien Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']  # Mets ici les vrais noms de tes champs s'ils sont différents
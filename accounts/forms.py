from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Adresse e-mail",
        widget=forms.EmailInput(attrs={'placeholder': 'exemple@email.com'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Libellés en français
        self.fields['username'].label = "Nom d'utilisateur"
        self.fields['username'].widget.attrs['placeholder'] = "Votre nom d'utilisateur"
        
        if 'password1' in self.fields:
            self.fields['password1'].label = "Mot de passe"
        if 'password2' in self.fields:
            self.fields['password2'].label = "Confirmation du mot de passe"

        # Supprime TOUS les messages d'aide sous les champs (mots de passe inclus)
        for field in self.fields.values():
            field.help_text = ''
            field.widget.attrs['class'] = 'form-control'
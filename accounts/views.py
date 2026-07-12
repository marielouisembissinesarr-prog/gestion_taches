from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        # On récupère manuellement ce que l'utilisateur a tapé dans ton HTML
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Petite vérification : est-ce que les deux mots de passe sont identiques ?
        if password != password_confirm:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'accounts/register.html')

        # Petite vérification : est-ce que le nom d'utilisateur existe déjà ?
        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà pris.")
            return render(request, 'accounts/register.html')

        # Si tout est bon, on crée l'utilisateur de manière sécurisée !
        user = User.objects.create_user(username=username, email=email, password=password)
        
        # On le connecte automatiquement
        login(request, user)
        
        # Hop, direction le tableau de bord !
        return redirect('dashboard')

    return render(request, 'accounts/register.html')
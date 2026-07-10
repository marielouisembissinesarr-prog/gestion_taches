from django.shortcuts import render, redirect
from .forms import ProjectForm

def home(request):
    return render(request, 'home.html')

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige vers l'accueil une fois créé
    else:
        form = ProjectForm()
    return render(request, 'projects/create_project.html', {'form': form})

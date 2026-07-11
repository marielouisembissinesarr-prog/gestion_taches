"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView  # On ajoute ça pour la redirection
from projects.views import create_project
from accounts.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Redirection magique : si Django cherche accounts/login/, on l'envoie sur login/
    path('accounts/login/', RedirectView.as_view(pattern_name='login', permanent=False)),
    
    # Route pour la création de projet
    path('projet/creer/', create_project, name='create_project'),
    
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('', include('django.contrib.auth.urls')),
]
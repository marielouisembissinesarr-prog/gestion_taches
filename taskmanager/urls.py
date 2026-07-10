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
from projects.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    
    # On force Django à utiliser notre fichier précis pour la connexion
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    
    # On garde le reste pour la déconnexion automatique
    path('', include('django.contrib.auth.urls')),
]
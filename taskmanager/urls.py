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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

try:
    User = get_user_model()
    # On crée le compte 'patron' automatiquement au démarrage du site
    if not User.objects.filter(username='patron').exists():
        User.objects.create_superuser('patron', 'patron@example.com', 'DerniereChance2026!')
        print("COMPTE PATRON CRÉÉ AVEC SUCCÈS SUR LE SITE WEB !")
except Exception as e:
    print(f"Erreur création auto : {e}")
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
from accounts import views  # On importe nos vues toutes neuves !

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # <-- On connecte la page d'accueil à notre fonction home !
]

# --- Ton code pour le compte patron (on le laisse) ---
from django.contrib.auth import get_user_model
try:
    User = get_user_model()
    if not User.objects.filter(username='patron').exists():
        User.objects.create_superuser('patron', 'patron@example.com', 'DerniereChance2026!')
except Exception as e:
    pass
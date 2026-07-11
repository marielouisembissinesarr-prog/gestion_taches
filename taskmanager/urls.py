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
from django.contrib.auth import views as auth_views
from accounts.views import register  # Ajuste si ta vue profil y est aussi
from projects import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentification
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
    
    # Application Projets & Tâches (Conforme section 5.2 du rapport)
    path('', views.dashboard, name='dashboard'),
    path('projet/creer/', views.projet_create, name='projet_create'),
    path('projet/<int:id>/', views.projet_detail, name='projet_detail'),
    path('projet/<int:id>/modifier/', views.projet_update, name='projet_update'),
    path('projet/<int:id>/supprimer/', views.projet_delete, name='projet_delete'),
    
    path('projet/<int:projet_id>/tache/creer/', views.tache_create, name='tache_create'),
    path('tache/<int:id>/', views.tache_detail, name='tache_detail'),
    path('tache/<int:id>/modifier/', views.tache_update, name='tache_update'),
    path('tache/<int:id>/supprimer/', views.tache_delete, name='tache_delete'),
]
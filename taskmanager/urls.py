from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import register_view, logout_view  # Tous les imports d'authentification ici
from projects import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentification
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),  # Notre vue de déconnexion personnalisée sécurisée
    path('register/', register_view, name='register'),
    
    # Application Projets & Tâches
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
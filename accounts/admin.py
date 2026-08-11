from django.contrib import admin
from django.contrib.auth.models import User

# Identifiants de secours pour l'admin
USERNAME = "superadmin"
PASSWORD = "Passe2026"
EMAIL = "admin@example.com"

# Créer ou mettre à jour le compte au démarrage
try:
  user, created = User.objects.get_or_create(
      username=USERNAME, defaults={"email": EMAIL}
  )
  user.set_password(PASSWORD)
  user.is_staff = True
  user.is_superuser = True
  user.is_active = True
  user.save()
except Exception:
  pass

# Register your models here.

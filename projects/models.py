from django.contrib.auth.models import User
from django.db import models


class Projet(models.Model):
  titre = models.CharField(max_length=200)
  description = models.TextField(blank=True, null=True)
  createur = models.ForeignKey(
      User, on_delete=models.CASCADE, related_name='projets_crees'
  )
  membres = models.ManyToManyField(
      User, related_name='projets_membres', blank=True
  )
  date_creation = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.titre


class Tache(models.Model):
  STATUT_CHOICES = [
      ('todo', 'À faire'),
      ('en_cours', 'En cours'),
      ('termine', 'Terminé'),
  ]

  PRIORITE_CHOICES = [
      ('basse', 'Basse'),
      ('moyenne', 'Moyenne'),
      ('haute', 'Haute'),
  ]

  projet = models.ForeignKey(
      Projet, on_delete=models.CASCADE, related_name='taches'
  )
  titre = models.CharField(max_length=200)
  description = models.TextField(blank=True, null=True)
  statut = models.CharField(
      max_length=20, choices=STATUT_CHOICES, default='todo'
  )
  priorite = models.CharField(
      max_length=20, choices=PRIORITE_CHOICES, default='moyenne'
  )
  # 📍 Nouveau champ pour assigner la tâche à un utilisateur :
  assigne_a = models.ForeignKey(
      User,
      on_delete=models.SET_NULL,
      null=True,
      blank=True,
      related_name='taches_assignees',
      verbose_name='Assigné à',
  )
  date_echeance = models.DateField(blank=True, null=True)
  date_creation = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.titre
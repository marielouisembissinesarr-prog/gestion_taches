from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from projects.models import Projet


class ProjetSecurityTests(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user(username='userA', password='Password123!')
        self.user_b = User.objects.create_user(username='userB', password='Password123!')
        self.projet_a = Projet.objects.create(titre="Projet A", createur=self.user_a)

    def test_creation_projet_solo(self):
        projet = Projet.objects.create(titre="Projet Solo", createur=self.user_a)
        self.assertEqual(projet.membres.count(), 0)

    def test_idor_projet_detail_refuse_non_membre(self):
        self.client.login(username='userB', password='Password123!')
        url = reverse('projet_detail', args=[self.projet_a.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)  # Accès refusé (Sécurité IDOR)

    def test_acces_autorise_createur(self):
        self.client.login(username='userA', password='Password123!')
        url = reverse('projet_detail', args=[self.projet_a.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Accès autorisé
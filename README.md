# 📋 Application de Gestion de Tâches (Django)

![Django CI](https://github.com/votre-nom-utilisateur/gestion_taches/actions/workflows/django-ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)
![Framework](https://img.shields.io/badge/framework-Django-092E20.svg)

Une application web complète de gestion de projets et de tâches collaboratives développée avec **Django** et **Bootstrap 5**.

---

## ✨ Fonctionnalités Principales

* **Gestion de compte utilisateur :**
  * Inscription sécurisée avec validation des mots de passe (`UserCreationForm`).
  * Connexion / Déconnexion sécurisées.
* **Gestion des Projets & Tâches :**
  * Création, modification et suivi de projets.
  * Attribution des tâches avec niveaux de priorité (*Basse*, *Moyenne*, *Haute*) et statuts (*À faire*, *En cours*, *Terminé*).
* **Sécurité renforcée :**
  * Protection contre les failles d'accès direct par ID (**IDOR**) via des vérifications de permissions strictes.
  * Protection contre les attaques **CSRF**.
* **Intégration Continue (CI/CD) :**
  * Pipeline **GitHub Actions** exécutant automatiquement les tests unitaires à chaque `push`.

---

## 🛠️ Technologies Utilisées

* **Back-End :** Python 3, Django
* **Front-End :** HTML5, CSS3, Bootstrap 5
* **Base de données :** SQLite (Développement/Tests)
* **Outillage & CI/CD :** Git, GitHub Actions, PowerShell / Bash

---

## 🚀 Installation et Lancement en Local

### Prerequisites
* Python 3.10+ installé sur votre machine.
* Git.

### 1. Cloner le dépôt
```bash
git clone [https://github.com/marielouisembissinesarr-prog/gestion_taches.git](https://github.com/marielouisembissinesarr-prog/gestion_taches.git)
cd gestion_taches
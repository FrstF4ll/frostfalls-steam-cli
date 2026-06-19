# Projet : Frostfall Steam Manager (CLI)

## 1. Vision du Projet
Frostfall est un gestionnaire de bibliothèque Steam minimaliste, sécurisé et performant, conçu pour les utilisateurs avancés (notamment sous Linux). L'objectif est d'automatiser l'installation et la maintenance des jeux via `steamcmd` tout en offrant une interface utilisateur propre et moderne dans le terminal.

## 2. Architecture Technique
- **Langage** : Python 3.14+
- **Gestionnaire de dépendances** : Poetry 2.0+
- **Bibliothèques clés** :
  - `vdf` : Parsing des fichiers Steam (.acf).
  - `requests` : Interaction avec l'API Steam Web.
  - `keyring` : Stockage sécurisé des identifiants.
  - `rich` : Interface utilisateur (UI) terminal.
  - `shutil` / `subprocess` / `pathlib` : Gestion système (StdLib).

## 3. User Stories (Backlog)

### Phase 1 : Initialisation & Environnement
- [ ] **US 1.1** : En tant qu'utilisateur, je veux que le programme vérifie automatiquement si `steamcmd` et 'steam' sont installés pour éviter les erreurs de lancement.
- [ ] **US 1.2** : En tant qu'utilisateur, je veux que le programme vérifie si le répertoire de destination est accessible en écriture.
- [ ] **US 1.3** : En tant qu'utilisateur, je veux que le programme valide la connectivité avec les serveurs Steam.

### Phase 2 : Gestion de la Bibliothèque
- [ ] **US 2.1** : En tant qu'utilisateur, je veux pouvoir lister les jeux installés en lisant les fichiers `.acf` du répertoire `steamapps`.
- [ ] **US 2.2** : En tant qu'utilisateur, je veux voir l'état (installé/à mettre à jour) de mes jeux via une interface `rich` propre.

### Phase 3 : Automatisation & Installation
- [ ] **US 3.1** : En tant qu'utilisateur, je veux pouvoir installer ou mettre à jour un jeu spécifique en utilisant `steamcmd` via une commande simple.
- [ ] **US 3.2** : En tant qu'utilisateur, je veux voir une barre de progression en temps réel lors du téléchargement/mise à jour.

### Phase 4 : Sécurité & Configuration
- [ ] **US 4.1** : En tant qu'utilisateur, je veux stocker mes identifiants Steam dans le gestionnaire de clés du système (keyring) pour ne jamais les écrire en clair.
- [ ] **US 4.2** : En tant qu'utilisateur, je veux pouvoir définir mes préférences (répertoire d'installation, préférences de log) dans un fichier `config.toml`.

## 4. Directives pour l'Agent IA
- **Modularité** : Le code doit être divisé en modules (`validator.py`, `library_parser.py`, `steam_interface.py`, `ui_manager.py`).
- **Robustesse** : Chaque interaction avec le système (OS) ou `steamcmd` doit être encapsulée dans une gestion d'erreurs explicite.
- **Style** : Privilégier la clarté et la maintenabilité. Utiliser le typage Python (`type hints`).
- **État actuel** : L'environnement de développement est configuré avec Poetry. La structure du projet est en phase de démarrage (implémentation de la vérification initiale).

## 5. Conventions de développement
- Utiliser `pathlib` pour tous les chemins.
- Utiliser `poetry run` pour l'exécution des commandes.
- Tout nouveau module doit être documenté succinctement via une Docstring.
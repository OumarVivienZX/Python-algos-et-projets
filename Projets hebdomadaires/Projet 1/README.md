# Projet 1 - Tic-Tac-Toe

Ce dépôt contient le premier projet hebdomadaire de mise à niveau en Python. Il s'agit d'une implémentation du jeu Tic-Tac-Toe (morpion) en Python.

## Contenu du dossier

- `main.py` : point d'entrée principal (actuellement vide ou minimal).  
- `src/TicTacToe.py` : fichiers sources principaux pour la logique du jeu.
- `Projet 1 (mise à niveau python.txt` : notes ou consignes de la mise à niveau en Python.  
- `Projet 1(Tic-Tac-Toe).md` : description initiale du projet (en markdown).  
- `.gitignore` : fichiers et dossiers ignorés par Git (notamment l'environnement virtuel `venv`).

## Objectif

L'objectif de ce projet est de créer un jeu Tic-Tac-Toe jouable en console, en mettant en œuvre :

- La gestion de la grille de jeu 3x3
- La détection de gagnant ou match nul
- La saisie utilisateur et validation des coups
- (Optionnel) Un adversaire IA simple ou un mode deux joueurs

## Installation et exécution

1. **Créer un environnement virtuel** (déjà présent sous `venv` mais vous pouvez en recréer un) :  
   ```bash
   python -m venv venv
   ```
2. **Activer l'environnement** :  
   - Windows : `venv\Scripts\activate`
3. **Installer les dépendances** (aucune pour ce projet, mais vous pouvez ajouter des modules si nécessaire).  
4. **Lancer le jeu** :  
   ```bash
   python main.py
   ```
   ou exécuter le module dans `src` selon la structure.

## Notes

- Le fichier `main.py` peut être utilisé pour orchestrer l'exécution du jeu.  
- Si vous souhaitez restructurer le projet, n'hésitez pas à ajouter un `requirements.txt` pour les dépendances.

---

*Ce README fournit un aperçu du projet Tic-Tac-Toe et des instructions de base pour commencer à travailler dessus.*
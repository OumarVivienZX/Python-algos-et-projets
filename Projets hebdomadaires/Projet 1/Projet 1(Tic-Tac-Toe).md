# Projet 1 : Créer un Jeu de Tic-Tac-Toe en Console

## Énoncé du Projet
Ce projet consiste à développer un jeu de Tic-Tac-Toe (Morpion) en mode console (terminal) pour pratiquer les bases de Python et de l'algorithmique. Il est conçu pour être concret et motivant, en te permettant de créer un jeu jouable dès le début de ton apprentissage.

## Objectif Final
Un programme Python qui permet à deux joueurs (humain vs humain, ou humain vs ordinateur) de jouer au Tic-Tac-Toe sur une grille 3x3. Le jeu affiche la grille, gère les tours, vérifie les victoires/nuls, et annonce le gagnant. À la fin, il propose de rejouer.

## Notions Python et Algorithmes de Base à Pratiquer
Ce projet t'oblige à utiliser un ensemble de notions fondamentales pour couvrir les bases de la programmation et de l'algorithmique :
- **Variables et types de données** : Stocker la grille (comme une liste de listes), les symboles des joueurs ('X' et 'O' comme chaînes), des compteurs pour les tours (entiers).
- **Input/Output** : Utiliser `input()` pour demander les coups aux joueurs, et `print()` pour afficher la grille et les messages.
- **Conditions (if/elif/else)** : Vérifier si une case est valide (libre ? dans la grille ?), détecter les victoires (lignes, colonnes, diagonales), ou si c'est un nul.
- **Boucles (while et for)** : Une boucle while pour le jeu principal (tant que pas de gagnant), des boucles for pour vérifier les lignes/colonnes/diagonales, ou pour itérer sur la grille.
- **Listes** : Représenter la grille comme une liste 2D (ex: `[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]`).
- **Fonctions** : Découper le code en fonctions pour la clarté, comme `afficher_grille()`, `verifier_gagnant()`, `jouer_coup()`.
- **Gestion d'erreurs basique** : Gérer les inputs invalides (ex: si le joueur entre un nombre hors grille, redemander avec une boucle).
- **Algorithmes simples** : Logique pour alterner les tours, recherche dans une liste (pour vérifier les alignements).

## Étapes Suggérées pour Découper le Projet
Pour t'aider à avancer pas à pas et éviter d'être submergé, voici une décomposition logique :
1. Crée une fonction pour afficher la grille (utilise des print avec des séparateurs comme '|' et '-').
2. Initialise la grille et les variables (joueur actuel, tours).
3. Dans une boucle while, demande l'input au joueur (ligne et colonne, ex: "Entrez ligne (0-2) et colonne (0-2) : "), vérifie si valide, place le symbole.
4. Après chaque coup, vérifie si victoire ou nul.
5. Alterne les joueurs.
6. À la fin, demande si rejouer (oui/non avec une autre boucle).

## Défis Bonus pour Complexifier
Si tu termines vite, ajoute ces éléments pour te challenger et te pousser à rechercher en ligne (Google, StackOverflow) :
- Ajoute un mode "humain vs ordinateur" : L'ordinateur choisit un coup aléatoire (utilise `random` module – `import random`), ou même une IA simple qui bloque les victoires imminentes (algorithme minimax basique, si tu oses rechercher ça !).
- Gère les erreurs avancées : Utilise `try/except` pour catcher si l'input n'est pas un entier.
- Améliore l'UX : Couleurs dans la console (recherche "ANSI colors in Python") ou une grille plus jolie.
- Stats : Compte les victoires et affiche un score à la fin de plusieurs parties.

## Consignes Générales
- **Code en Python pur** : Pas besoin de bibliothèques externes pour ce projet, sauf `random` si bonus.
- **Rends-le lisible** : Utilise des commentaires (#) pour expliquer ton code.
- **Teste-le bien** : Joue plusieurs parties pour voir les bugs.
- **Rendu** : Quand fini, envoie-moi ton code pour correction détaillée (ce qui est bien, améliorations, bugs, explications).
- **Durée** : Une semaine (jusqu'au lundi prochain), mais dis-moi si besoin de plus de temps.
- **Aide** : Pose des questions pendant la semaine pour guidance sans spoilers.

Bonne chance! Ce projet va te faire toucher à toutes les bases d'algorithmique en Python de manière pratique. Lance-toi et dis-moi si tu as besoin d'un coup de pouce initial. 😊
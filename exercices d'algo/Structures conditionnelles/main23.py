annee = int(input("Entrez l'année :"))

if ((annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0) ):
    print(f" l'année {annee} est une année bisextille.")
else :
    print(f" l'année {annee} n'est pas une année bisextille")

# une année bisextille est une année qui compte 366 jours au lien de 365 jours.
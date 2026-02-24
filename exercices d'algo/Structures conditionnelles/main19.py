PHT = float(input("Entrez le prix Hors taxe de votre produit : "))
A = 7/100
B = 20/100
C = 25 /100

Categorie = input ("Entrez la catégorie du produit :")


if Categorie == "A" :
    TVA = PHT * A
    TTC = PHT + TVA
    print(f" Le TTC de votre produit de catégorie{Categorie} est de {TTC} $")

elif Categorie == "B" :
    TVA = PHT * B
    TTC = PHT + TVA
    print(f" Le TTC de votre produit de catégorie{Categorie} est de {TTC} $")  
elif Categorie == "C" :
    TVA = PHT * C
    TTC = PHT + TVA
    print(f" Le TTC de votre produit de catégorie{Categorie} est de {TTC} $")

else : 
    print("La catégorire de votre article n'est pas répertorié")
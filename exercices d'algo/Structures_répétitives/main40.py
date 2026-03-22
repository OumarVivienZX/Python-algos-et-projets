N  = int(input("Veuillez entrer la valeur de l'entier à calculer : "))
nbr = 0
M = N
while N != 0 :
    nbr += 1
    N = N // 10

print(f" L'entier {M} contient {nbr} chiffres. ")
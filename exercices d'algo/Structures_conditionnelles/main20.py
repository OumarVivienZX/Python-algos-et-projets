A =  int(input (" Entrez le premier nombre entier : "))
B =  int(input (" Entrez le Deuxième nombre entier : "))
calcule = 0
operation = input("Quel opération voulez vous effectuer ? :")

if operation == "+" :
    calcule = (A + B)
    print(f" {A} {operation} {B} = {calcule}")
elif operation == "-" :
    calcule = (A - B)
    print(f" {A} {operation} {B} = {calcule}")
elif operation == "*" :
    calcule = (A * B)
    print(f" {A} {operation} {B} = {calcule}")
elif operation == "/" :
    if B != 0 :
        calcule = (A / B)
        print(f" {A} {operation} {B} = {calcule}")
    else : 
        print("la division par 0 est impossible")
    
else :
    print(" l'opération choisie n'est pas répertoriée")

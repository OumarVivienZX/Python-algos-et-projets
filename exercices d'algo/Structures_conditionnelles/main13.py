A = int(input("A = "))
B = int(input("B = "))

if (A*B) > 0 :
    C = B
    B = A
    A = C

    print(f" A = {A}")
    print(f" B = {B}")

else : 

    somme = A + B
    produit = A * B
    A = somme
    B = produit
    print(f" A = {A}")
    print(f" B = {B}")




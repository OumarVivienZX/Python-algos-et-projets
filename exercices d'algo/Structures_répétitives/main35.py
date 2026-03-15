n = int(input("Entrez un nombre entier n supérieur à 2: "))

while n <2 :
    n = int(input("Entrez un nombre entier n supérieur à 2: "))

U0  = 0
U1 = 1
U = 0
print("Les termes de la suite de Fibonacci sont :")
print("U0 = 0")
print("U1 = 1")

for i in range(2, n + 1) :# on commence à 2 car U0 et U1 sont déjà définis
    U = U0 + U1
    print(f"U{i} = {U}")
    U0 = U1
    U1 = U





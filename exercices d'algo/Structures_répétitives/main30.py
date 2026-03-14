n = int(input("Entrer la valeur de l'entier n :"))

J = 1
S = 0

for i in range(n):
    print(f" S = {S} + {J}^2")
    S = S + J**2
    J = J + 2

print("S = ", S)
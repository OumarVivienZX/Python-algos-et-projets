N = int(input("Veuillez entrer la valeur de l'entier à calculer : "))
M = N
inverse = 0

while N != 0 :
    inverse = (inverse * 10) + (N % 10)
    print(inverse)
    N = N // 10
    print(N)

print (" L 'inverse de ",M ,"est ",inverse)
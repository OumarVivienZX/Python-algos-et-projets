N = int(input("veuillez entrer un nombre entier : "))
#déterminer si un nombre est premier ou pas
if N < 2 :
    print(f"{N} n'est pas un nombre premier.")
else :
    is_prime = True
    for i in range(2, (N//2) + 1) :
        if N % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{N} est un nombre premier.")
    else:
        print(f"{N} n'est pas un nombre premier.")
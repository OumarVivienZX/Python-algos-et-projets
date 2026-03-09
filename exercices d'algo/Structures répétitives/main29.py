n = int(input("Entrez un nombre réel : "))
fac = 1
if n < 0 :
    print("Veuillez entrer un nombre réel positif ")

elif n == 0 :
    print(f"{n}! = 1 ")
else :
    for i in range ( 1 , n+1):
        fac *= i
        
    print(f"{n}! = {fac}")


a = int(input("veuillez entrer la valeur du premier nombre :"))
b = int(input("veuillez entrer la valeur du premier nombre :"))


if a > b :
    min = b
else :
    min = a 


for i in range(1 , min + 1) :
    if a % i == 0 and b % i == 0 :
        pgcd = i

print(" Le PGCD de",a,"et",b,"est",pgcd)

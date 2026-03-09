n = int(input("Entrez la valeur de n : "))
while n <= 0 :
    n = int(input("Entrez la valeur de n : "))

for i in range (1, n+1):
    if n % i  == 0 :
        print (str(i)+", " , end="")
    
print(" Sont des diviseurs de " + str(n))
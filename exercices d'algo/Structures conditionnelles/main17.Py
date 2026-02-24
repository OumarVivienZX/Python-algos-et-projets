import math
print ("Nous allons résoudre une équation du second degré de la forme ax^2 + bx + c = 0")
a = int(input("Veuillez entrer la valeur de a : "))
b = int(input("Veuillez entrer la valeur de b : "))
c = int(input("Veuillez entrer la valeur de c : "))

delta = b**2 - 4 * a * c

if delta > 0 : 

    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    
    print (" Nous avons deux solutions réelles : ")

    print(f"X1 = {x1: .2f}")
    print(f"X2 = {x2: .2f}")
    print(f"({x1: .2f} , {x2 : .2f})")


elif delta == 0 : 
    x0 = (-b) / (2*a) 
    print (f" Nous avons une seul solution réelle X0 = {x0 : .2f} ")

else : 
    print (" L'équation n'a pas de solution.")

    

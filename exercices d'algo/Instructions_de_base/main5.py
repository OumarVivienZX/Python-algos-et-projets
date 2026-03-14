print("**************Bienvenu à vous dans le program opérations******************")
print("**************************************************************************")
A = int(input("Veuillez entrer la valeur de A : "))
B = int(input("Veuillez entrer la valeur de B : "))


print("------------ A: Addition---------------")
print("------------ B: Soustraction---------------")
print("------------ C: Multiplication---------------")
print("------------ D: Division---------------")
reponse = input("Quel opération voulez vous faire ? :")

if reponse == "A" :
    print (f"l'addition de {A} par {B} donne :{A+B}")
    
elif reponse == "B" :
    print (f"la soustraction de {A} par {B} donne : {A-B}")

elif reponse == "C" :
    print (f"la multiplication de {A} par {B} donne : {A*B}")  

elif reponse == "D" :
    print (f"la division de {A} par {B} donne : {A/B}")

else :
    print(" Ce choix ne fait pas partie du programme")
    
   
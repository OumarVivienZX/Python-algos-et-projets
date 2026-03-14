age = int (input(" Entrez l'age de Amal : "))

while age <= 0 :
    age = int (input(" Entrez l'age de Amal : "))
    
somme = 0
for i in range (1, age + 1) :
    compte = (500 + (3 * i))
    somme += compte 

print(f" Le compte de Amal à son {age}ième anniverssaire est de {somme}dh")
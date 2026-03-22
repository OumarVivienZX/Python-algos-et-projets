import random

N = random.randint(1 , 30)
essais = 5 
print(" J'ai choisi un nombre entre 1 et 30. Vous avez 5 essais pour le deviner.")

for i in range(1, essais + 1) :
    réponse = int(input(" quel est le nombre ? :"))
    if réponse == N : 
        print(f" Félicitation , vous avez réussi à trouver le nombre {N} en {i} tentatives.")
        break
    elif réponse > N :
        print("C'est moins !")
    elif réponse < N :
        print("C'est plus")
if réponse != N :
    print(f" Désolé , vous avez épuisé vos 5 essais. Le nombre était {N}.")
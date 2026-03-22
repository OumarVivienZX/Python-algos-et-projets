N = int (input("Veuillez saisir le nombre d'équipe qui participent au championnat :"))

for i in range(1 , N+1) :
    for j in range(1 , N+1):
        if i != j :
            print(f" Equipe {i} Vs Equipe {j}")

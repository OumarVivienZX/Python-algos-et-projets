n = int(input("Entrez un nombre entier correpondant au rang de la suite n: "))

Uo = 6
Un = 0
for i in range(1, n + 1) :
    Un = 4 * Uo + 10
    Uo = Un
    print(f" U{i} = {Un}")

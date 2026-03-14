N = int(input("Veuillez entrer le nombre de copies à faire : "))
P = 0

if N <= 10:
    P = N * 0.30

elif N <= 30:
    P = 10 * 0.30 + (N - 10) * 0.25

else:
    P = 10 * 0.30 + 20 * 0.25 + (N - 30) * 0.20

print(f"La facture des {N} copies est de {P} dh")
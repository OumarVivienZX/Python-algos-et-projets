n = int (input("Entrez une valeur pour n : "))
s = 0
for i in range (n + 1) :
    s += 10 ** i
    print(f" S = 10^{i}") 

print(f" S = {s}")
n = int (input("Entrez un nombre : "))
i = 1
s = 0

for i in range( i, n + 1): 
    print(f" S = 1 / {s : .2f} + 1 / {i}") 
    s += 1 / i
    
print(f" S = {s : .2f}" )
T =  int(input("Entrer la valeur  en secondes :"))

H = T // 3600
M = (T % 3600) //60
S = (T % 3600) %60

print (f" {T} = {H}h {M}m {S}s")
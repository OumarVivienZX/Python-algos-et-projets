note = 0
i = 1 
somme = 0
for i in range(1, 6):
    note  =  float(input(f"entrer la note n° {i}:"))
    somme += note
    i += 1

moyenne = (somme /  5)
print(f" la somme des notes est {somme}")
print(f" la moyenne est {moyenne}")

import math
rayon = float(input("Veuillez entrer le rayon de la sphère : "))
volume = (4*math.pi*(rayon**3)) / 3

print(f" le volume de la sphère de rayon {rayon} est de : {volume: .2f}")
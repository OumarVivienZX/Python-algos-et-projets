import math 
Xa = float(input(" Veuillez entrer la cordonnée Xa : "))
Xb = float(input(" Veuillez entrer la cordonnée Xb : "))
Ya = float(input(" Veuillez entrer la cordonnée Ya : "))
Yb = float(input(" Veuillez entrer la cordonnée Yb : "))

AB = math.sqrt((Xb - Xa)**2 +(Yb - Ya)**2)

print(f"La distance AB est : {AB: .2f}")
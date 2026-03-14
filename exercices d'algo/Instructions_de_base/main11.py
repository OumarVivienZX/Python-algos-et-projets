print ("veuillez entrer lea valeur des trois résitances : ")
R1 = float(input("R1 : "))
R2 = float(input("R2 : "))
R3 = float(input("R3 : "))

Rser = (R1 + R2 +R3)
Rpar = (R1 * R2 * R3) / ((R1 * R2) + (R1 * R3) + (R2 * R3))

print((f"La résistance en série est : {Rser : .2f}"))
print((f"La résistance en parallèle est : {Rpar : .2f}"))

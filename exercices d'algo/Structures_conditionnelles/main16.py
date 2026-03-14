note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))    
note3 = float(input("Entrez la troisième note : "))


moyenne = (note1 + note2 + note3) / 3
print("La moyenne est : ", format(moyenne, ".2f"))
if moyenne >= 16 : 
    print("Mention : Très bien")
elif 16 > moyenne >= 14 : 
    print("Mention : Bien")
elif 14 > moyenne >= 12 : 
    print("Mention : Assez bien")
elif 12 > moyenne >= 10 : 
    print("Mention : Passable")
else :    print("Mention : Insuffisant")    

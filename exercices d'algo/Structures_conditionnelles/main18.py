age = int(input("veuillez entrer votre age :"))
sexe = input("veuillez entrer votre sexe :")


if sexe == "H" and age >= 20 :
    print(" Vous êtes imposable.")

elif sexe == "F" and 18 <= age <= 35 :
        print("Vous êtes imposable.")

else : 
    print("Vous n'êtes pas imposable.")

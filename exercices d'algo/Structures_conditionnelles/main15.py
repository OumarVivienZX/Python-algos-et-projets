age = int(input("Quel est votre age ? :"))

if age >=6 and age <= 7  :
    print(f" vous avez {age} ans vous êtes donc Poussin")

elif age >= 8 and age <= 9 :
    print(f" vous avez {age} ans vous êtes donc Pupille")

elif age >= 10 and age <= 11 :
    print(f" vous avez {age} ans vous êtes donc Minime")

elif age >= 12 and age <= 16 :
    print(f" vous avez {age} ans vous êtes donc Cadet")

else :
    print (" votre catégorie n'est pas répertoriée")
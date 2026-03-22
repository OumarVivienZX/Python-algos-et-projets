choix = "O"

while choix  == "O" :# Menu de la calculatrice python
    print("""Bienvenue dans la calculatrice Python !

    Veuillez choisir une opération :
    1. Addition
    2. Soustraction
    3. Multiplication
    4. Division
    5. Modulo
    6. Puissance""")

    opération = input("Entrez le numéro de l'opération que vous souhaitez effectuer : ")
    n1 = float(input("Entrez le premier terme de l'opération : "))
    n2 = float(input("Entrez le deuxième terme de l'opération : "))

    if opération == "1" :   
        résultat = n1 + n2
        print(f"Le résultat de l'addition est : {résultat}")    
    elif opération == "2" :
        résultat = n1 - n2
        print(f"Le résultat de la soustraction est : {résultat}")       
    elif opération == "3" : 
        résultat = n1 * n2
        print(f"Le résultat de la multiplication est : {résultat}")
    elif opération == "4" :
        if n2 != 0 :
            résultat = n1 / n2
            print(f"Le résultat de la division est : {résultat}")
        else :
            print("Erreur : Division par zéro n'est pas autorisée.")
    elif opération == "5" :
        if n2 != 0 :
            résultat = n1 % n2
            print(f"Le résultat du modulo est : {résultat}")
        else :
            print("Erreur : Modulo par zéro n'est pas autorisé.")
    elif opération == "6" :
        résultat = n1 ** n2
        print(f"Le résultat de la puissance est : {résultat}")

    choix = input("Voulez-vous effectuer une autre opération ? (O/N) : ").upper()
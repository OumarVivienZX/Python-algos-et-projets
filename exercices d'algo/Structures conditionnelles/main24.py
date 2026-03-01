caractere = input ("Entrez un caractère : ")

if "A" <= caractere <= "Z" or "a" <= caractere <= "z" : 
    print(f" Le caratère {caractere} est une lettre.")
elif "0" <= caractere <= "9" :
    print(f"Le caractère {caractere} est un chiffre.")
else :
    print(f" Le caractère {caractere} est un symbole.")

# caractere = input("Entrez un caractère : ")

# if caractere.isalpha():
#     print("Le caractère est une lettre.")
# elif caractere.isdigit():
#     print("Le caractère est un chiffre.")   
# else:
#     print("Le caractère est un symbole.")

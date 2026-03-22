N = int(input("Entrer le nombre à comparer : "))
M = N
inverse = 0

while N != 0 :
    inverse = (inverse * 10) + (N % 10)
    N = N // 10
    
if M == inverse : 
    print(f"Le nombre {M} est un parlindrome")
else :
    print(f"Le nombre {M} n'est pas un palindrome")
p_mar = 1000000
p_aga = 500000
i = 0

while p_mar >= p_aga :

    p_mar += 50000
    print(f" population Marrakech : {p_mar: .2f}")

    p_aga  = p_aga * (1.08)
    print(f" population Agadir    : {p_aga: .2f}")

    i += 1
    print(f" {i} ième année" )
    print("-" * 50)

print(f"La population d'Agadir dépasse la populaton de Marrakech à la {i} ième année")

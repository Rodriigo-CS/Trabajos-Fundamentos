Num = int(input("Ingrese hasta que número analizará su divisores: "))
for i in range(1, Num + 1):
    if i % 2 == 0:
        Divisores = str("Es divisible por ") + str(2)
    if i % 3 == 0:
        Divisores = str("Es divisible por ") + str(3)
    if i % 5 == 0:
        Divisores = str("Es divisible por ") + str(5)
    if i % 2 == 0 and i % 3 == 0:
        Divisores = str("Es divisible por ") + str(2) + str(" y ") + str(3)
    if i % 2 == 0 and i % 5 == 0:
        Divisores = str("Es divisible por ") + str(2) + str(" y ") + str(5)
    if i % 3 == 0 and i % 5 == 0:
        Divisores = str("Es divisible por ") + str(3) + str(" y ") + str(5)
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        Divisores = str("Es divisible por ") + str(2) + str(",") + str(3) + str(" y ") + str(5)
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        Divisores = "No tiene divisores"
    print(i, Divisores)
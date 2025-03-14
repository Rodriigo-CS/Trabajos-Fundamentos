Num = int(input("Ingrese un número mayor o igual 2: "))
for n in range(2, Num+1):
    Divisores = 0
    i = 2
    while i < n:
        if n % i == 0:
            Divisores = Divisores + 1
        i = i + 1
    if Divisores == 0:
        Primo = n
print("El número primo más cercano a", Num, "es:", Primo)
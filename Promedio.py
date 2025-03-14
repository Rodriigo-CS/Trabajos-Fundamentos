CantNum = int(input("Ingrese la cantidad de números va a promediar: "))
Promedio = 0
Cantidad = 0
for i in range(CantNum):
    Num = float(input("Ingrese un número: "))
    if Num % 2 == 0:
        Cantidad = Cantidad + 1
        Promedio = Promedio + Num
    else:
        pass
print("El promedio de los números pares es: ", Promedio / Cantidad)
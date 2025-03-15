Num = int(input("Ingrese un número: "))
Num0 = 0
ConteoP = 0
SumaP = 0
ConteoN = 0
SumaN = 0
if Num < 0:
    print("El número es negativo.")
    ConteoN += 1
    SumaN += Num
elif Num == 0:
    print("El número es cero.")
    Num0 = 1
else:
    print("El número es positivo.")
    ConteoP += 1
    SumaP += Num
while Num != 0:
    X = int(input("Ingrese un número: "))
    Num = X + Num
    print("El Número Acumulado es: ", Num)
    if X < 0:
        ConteoN += 1
        SumaN += X
    elif X > 0:
        ConteoP += 1
        SumaP += X
    else:
        pass
if Num0 == 1:
    print("No se ingresaron números positivos ni negativos.")
else:
    print("La cantidad de números positivos son: ", ConteoP)
    print("La cantidad de números negativos son: ", ConteoN)
    print("El promedio de los números positivos es: ", SumaP/ConteoP)
    print("El promedio de los números negativos es: ", SumaN/ConteoN)
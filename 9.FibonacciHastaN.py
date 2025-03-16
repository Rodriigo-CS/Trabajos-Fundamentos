Num = int(input("Ingrese el Valor Maximo que Tendrá la Sucesion de Fibonacci: "))
if Num == 0:
    print("0")
else:
    Terminos = False
    penultimo = 0
    ultimo = 1
    i = 2
    print(penultimo)
    print(ultimo)
    while Terminos == False:
        suma = penultimo + ultimo
        penultimo = ultimo
        ultimo = suma
        if ultimo > Num:
            Terminos = True
        else:
            print(ultimo)
            i = i + 1
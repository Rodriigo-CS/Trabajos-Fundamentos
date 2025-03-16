Num = int(input("Introduzca un número: "))
Fibonnaci = False
penultimo = 0
ultimo = 1
i = 2
if Num == 0:
    print("El siguiente termino de fibonacci es 1")
elif Num == 1:
    print("Existen dos terminos en la sucesion de Fibonnacci que son posteriores al 1: El numero 1 y el numero 2")
else:
    while Fibonnaci == False:
        if ultimo > Num:
            print("El siguiente termino de fibonnacci es ", ultimo)
            Fibonnaci = True
        else:
            suma = penultimo + ultimo
            penultimo = ultimo
            ultimo = suma
            i = i + 1
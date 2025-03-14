Proceso = True#Variable para controlar el ciclo
while Proceso == True:#Ciclo para repetir el proceso
    Num1 = int(input("Ingrese el primer número: "))
    Num2 = int(input("Ingrese el segundo número: "))
    Operacion = input("Ingrese la operación a realizar(+,-,*,/): ")
    if Operacion == "+":#Condicionales para analizar la operación requerida
        print("El resultado de la suma es: ",Num1+Num2)
    elif Operacion == "-":
        print("El resultado de la resta es: ",Num1-Num2)
    elif Operacion == "*":
        print("El resultado de la multiplicación es: ",Num1*Num2)
    elif Operacion == "/" and Num2 != 0:#Si el segundo numero es 0 no se puede realizar la división
        print("El resultado de la división es: ",Num1/Num2)
    else:
        print("Operación no válida, intentelo de nuevo")#Mensaje de error si no se ingreso ninguna operacion valida
    if input("Desea continuar o salir: ") == "salir" or "Salir":#Condicion para salir del ciclo
        Proceso = False
print("Fin del programa")
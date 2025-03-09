Num = int(input("ingrese un numero a convertir: "))
NumZ = Num #Variable para guardar el valor original de Num
B = int(input("Ingrese una base mayor o igual 2 y menor a 10: "))
Resultado = "" #Variable para ir añadiendo los residuos en cadena, empieza vacio para no alterar el número
Rango = False #Variable para mantener el ciclo While
if B <= 2 and B > 10:
    print("El numero no esta en el rango")
else:
    while Rango == False: #Ciclo While para obtener los residuos de Num en base B
        N = Num % B
        Num = Num // B
        Resultado = str(Resultado) + str(N)
        if Num < B: #Condicion para detener el ciclo
            Rango = True
print("El numero", (NumZ), "en base", (B), "es", str(Num) + str(Resultado))
Num = int(input("Ingrese un número: "))
Numz = Num
Resultado = ""
Rango = False
while Rango == False:
    N = Num % 2
    Num = Num // 2
    Resultado = str(N) + str(Resultado)
    if Num < 2:
        Rango = True
print ("El número", Numz, "en base 2 es", str(Num) + str(Resultado))
Num = Numz
Resultado = ""
Rango = False
while Rango == False:
    N = Num % 4
    Num = Num // 4
    Resultado = str(N) + str(Resultado)
    if Num < 4:
        Rango = True
print ("El número", Numz, "en base 4 es", str(Num) + str(Resultado))
Num = Numz
Resultado = ""
Rango = False
while Rango == False:
    N = Num % 8
    Num = Num // 8
    Resultado = str(N) + str(Resultado)
    if Num < 8:
        Rango = True
print ("El número", Numz, "en base 8 es", str(Num) + str(Resultado))
Num = Numz
Resultado = ""
Rango = False
while Rango == False:
    N = Num % 16
    Num = Num // 16
    if N == 10:
        N = "A"
    elif N == 11:
        N = "B"
    elif N == 12:
        N = "C"
    elif N == 13:
        N = "D"
    elif N == 14:
        N = "E"
    elif N == 15:
        N = "F"
    Resultado = str(N) + str(Resultado)
    if Num < 16:
        Rango = True
print ("El número", Numz, "en base 16 es", str(Num) + str(Resultado))
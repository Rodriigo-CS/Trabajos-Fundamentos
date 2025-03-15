Num1 = int(input("Ingrese un número: "))
Num2 = int(input("Ingrese un segundo número: "))
n = min(Num1, Num2)
m = max(Num1, Num2)
i = 2
K = 1
if Num1 % 2 == 0 and Num2 % 2 == 0 or Num1 % 2 == 1 and Num2 % 2 == 1:
    while i <= n:
        if Num1 % i == 0 and Num2 % i == 0:
            Num1 = Num1 / i
            Num2 = Num2 / i
            n = min(Num1, Num2)
            K = K * i
        else:
            i = i + 1
    print("El Maximo Común Divisor es", K)
elif Num1 % 2 == 0 and Num2 % 2 == 1 or Num1 % 2 == 1 and Num2 % 2 == 0:
    while m > 1:
        if Num1 % i == 0:
            Num1 = Num1 / i
            m = max(Num1, Num2)
            K = K * i
        elif Num2 % i == 0:
            Num2 = Num2 / i
            m = max(Num1, Num2)
            K = K * i
        else:
            i = i + 1
    print("El Minimo Común Múltiplo es", K)
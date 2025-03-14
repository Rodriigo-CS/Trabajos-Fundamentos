Num = int(input("Ingrese el número maximo de la lista: "))
for i in range(0,Num + 1):#El range va de 0 a Num + 1 para que el número ingresado sea incluido en la lista
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:#Se evalua si el número es divisible entre 2, 3 o 5 utilizando el or
        print(i)
    else:
        pass#Si no es divisible entre 2, 3 o 5 el número no se imprime y continua el ciclo
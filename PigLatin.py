Palabra = input("Ingrese una palabra: ")
if Palabra == "" or Palabra == " ":#Valida si la palabra ingresada es vacia o solo contiene espacios
    print("No ingreso ninguna palabra")
else:
    Letra = Palabra[0]#Guarda la primera letra de la palabra
    Palabra = Palabra[1:]#Guarda la palabra sin la primera letra
    print (Palabra + Letra + "ay")#Imprime la palabra sin la primera letra y la primera letra seguida de "ay"
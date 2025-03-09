Frase = input("Escriba una frase: ")
N = len(Frase)#Número de caracteres de la frase
Palabra = ""#Variable que almacenará las palabras de la frase
for i in range(0, N):#Ciclo que recorre la frase
    if Frase[i] == " ":#Si el ciclo detecta un espacio, Imprime la palabra que iba antes de ese espacio, para despues reiniciar la variable Palabra
        print(Palabra)
        Palabra = ""
    else:#Si no detecta un espacio, la variable Palabra se va llenando con las letras de la frase
        Palabra = Palabra + Frase[i]
print(Palabra)#Imprime la última palabra de la frase al no haber un espacio después de ella

    


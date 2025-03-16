Num = int(input("Ingrese un número: "))
N = len(str(Num))
Cifras = ""
for i in range(0, N):
        if (str(int(str(Num)[i])+1)) == "10":
              Cifras = Cifras + "0"
        else:
              Cifras = Cifras + (str(int(str(Num)[i])+1))
print(Cifras)

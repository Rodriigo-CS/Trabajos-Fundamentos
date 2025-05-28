a = []
b = []
c = []
print("Bienvenido")
print("Este programa resolvera un sistema de ecuaciones lineales 3x3 usando GAUSS-JORDAN")
for i in range (4):
    k  = 1 #Numero de ecuacion
    Variables = ["x", "y", "z"]
    if i == 3:
        print(f"Ingrese el resultado de la ecuacion {k}")
        a.append(float(input()))
    else:
        print(f"Ingrese el coeficiente de la variable {Variables[i]} de la ecuacion {k}")
        a.append(float(input()))
for i in range (4):
    k  = 2 #Numero de ecuacion
    Variables = ["x", "y", "z"]
    if i == 3:
        print(f"Ingrese el resultado de la ecuacion {k}")
        b.append(float(input()))
    else:
        print(f"Ingrese el coeficiente de la variable {Variables[i]} de la ecuacion {k}")
        b.append(float(input()))
for i in range (4):
    k  = 3 #Numero de ecuacion
    Variables = ["x", "y", "z"]
    if i == 3:
        print(f"Ingrese el resultado de la ecuacion {k}")
        c.append(float(input()))
    else:
        print(f"Ingrese el coeficiente de la variable {Variables[i]} de la ecuacion {k}")
        c.append(float(input()))
print("Sistema de ecuaciones:")
print(a)
print(b)
print(c)
#Verificamos que el sistema es correcto
    #HORA DE HACER EL METODO DE GAUSS-JORDAN
pasara = False

if a[0] != 1:
    inverso = 1/a[0]
    a = [x * inverso for x in a]

z = b[0]
y = c[0]

b = [b[x] - (a[x] * z) for x in range(4)]
c = [c[x] - (a[x] * y) for x in range(4)]

if b[1] != 1:
    inverso = 1/b[1]
    b = [x * inverso for x in b]

z = a[1]
y = c[1]
a = [a[x] - (b[x] * z) for x in range(4)]
c = [c[x] - (b[x] * y) for x in range(4)]

if c[2] != 1:
    inverso = 1/c[2]
    c = [x * inverso for x in c]

z = a[2]
y = b[2]
a = [a[x] - (c[x] * z) for x in range(4)]
b = [b[x] - (c[x] * y) for x in range(4)]

#Ya tendriamos todas las variables en 1

print(f"El valor de x es: {a[3]}")
print(f"El valor de y es: {b[3]}")
print(f"El valor de z es: {c[3]}")
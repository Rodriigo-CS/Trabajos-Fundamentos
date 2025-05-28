import matplotlib.pyplot as plt
import random as rnd

n = int(input("Ingresa la cantidad de elementos de la lista: "))
X = []
Y = []
for i in range(n):
    X.append(rnd.random())
    Y.append(rnd.random())

sumXpY = 0
sumX2 = 0
sumX = 0
sumY = 0
for i in range(n):
    sumXpY = sumXpY + (X[i] * Y[i])
    sumX2 = sumX2 + X[i]**2
    sumX = sumX + X[i]
    sumY = sumY + Y[i]
    
m = ((n * sumXpY) - (sumX * sumY)) / ((n * sumX2) - (sumX**2))   
b = ((sumY * sumX2) - (sumX * sumXpY)) / ((n * sumX2) - (sumX**2))

Y2 = []
for i in X:
    Y2.append(i*m + b)

plt.plot(X, Y, "g*", X, Y2, "r-")
plt.show()
import matplotlib.pyplot as plt
import random as rnd

N = 10
X = []
Y = []
XY = []
X2 = []

for i in range(N):
    X.append(rnd.randint(100,200))
    Y.append(rnd.randint(50,100))
    XY.append(X[i]*Y[i])
    X2.append(X[i]**2)

m = (N*sum(XY)-sum(X)*sum(Y))/(N*sum(X2)-(sum(X)**2))
b = (sum(Y)*sum(X2)-sum(X)*sum(XY))/(N*sum(X2)-(sum(X)**2))

Recta = []
for i in range(len(X)):
    Recta.append(m*(X[i]) + b)
plt.plot(X, Recta, 'r-', X, Y, 'bo')
plt.show()
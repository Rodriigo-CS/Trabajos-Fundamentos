import numpy as np

# Matriz aumentada
matriz = np.array([
    [0.6, 0.3, 0.1, 40],
    [0.2, 0.5, 0.3, 30],
    [0.1, 0.2, 0.7, 20]
], dtype=float)

# Eliminación de Gauss
n = 3
for i in range(n):
    # Pivoteo
    max_row = i + np.argmax(np.abs(matriz[i:, i]))
    matriz[[i, max_row]] = matriz[[max_row, i]]

    # Normalización del pivote
    matriz[i] = matriz[i] / matriz[i, i]

    # Eliminación hacia abajo
    for j in range(i+1, n):
        matriz[j] = matriz[j] - matriz[i] * matriz[j, i]

# Sustitución hacia atrás
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = matriz[i, -1] - np.sum(matriz[i, i+1:n] * x[i+1:n])

print("Solución usando eliminación de Gauss:")
print(f"x = {x[0]:.2f}, y = {x[1]:.2f}, z = {x[2]:.2f}")
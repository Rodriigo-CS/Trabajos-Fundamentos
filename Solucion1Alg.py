import numpy as np

# Coeficientes del sistema
A = np.array([
    [0.6, 0.3, 0.1],
    [0.2, 0.5, 0.3],
    [0.1, 0.2, 0.7]
])

# Términos independientes
b = np.array([40, 30, 20])

# Resolviendo el sistema
solucion = np.linalg.solve(A, b)

print("Solución usando numpy.linalg.solve:")
print(f"x = {solucion[0]:.2f}, y = {solucion[1]:.2f}, z = {solucion[2]:.2f}")
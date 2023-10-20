#Algoritmo Hacia Delante-Atr�s
import numpy as np

# Definici�n del modelo oculto de Markov
# Matrices de transici�n de estado (A) y probabilidades de observaci�n (B)
A = np.array([[0.7, 0.3],
              [0.4, 0.6]])
B = np.array([[0.1, 0.4, 0.5],
              [0.7, 0.2, 0.1]])

# Secuencia de observaciones
observaciones = [0, 1, 2, 2, 1, 0]

# Inicializaci�n de variables
num_estados = A.shape[0]
T = len(observaciones)

# Algoritmo hacia adelante
forward = np.zeros((num_estados, T))
for t in range(T):
    if t == 0:
        forward[:, t] = 1 / num_estados * B[:, observaciones[t]]
    else:
        forward[:, t] = B[:, observaciones[t]] * np.dot(A.T, forward[:, t - 1])

# Algoritmo hacia atr�s
backward = np.zeros((num_estados, T))
for t in range(T - 1, -1, -1):
    if t == T - 1:
        backward[:, t] = 1
    else:
        backward[:, t] = np.dot(A, B[:, observaciones[t + 1]] * backward[:, t + 1])

# Calcular la probabilidad de la secuencia de observaciones
probability = np.sum(forward[:, -1])

# Imprimir la probabilidad
print("Probabilidad de la secuencia de observaciones:", probability)

import random

# Definimos los estados y las probabilidades de transici�n
estados = ['A', 'B']
matriz_transicion = {
    'A': {'A': 0.7, 'B': 0.3},
    'B': {'A': 0.4, 'B': 0.6}
}

# Funci�n para realizar una transici�n de estado
def transicion_estado(estado_actual):
    return random.choices(list(matriz_transicion[estado_actual].keys()), list(matriz_transicion[estado_actual].values()))[0]

# Simulaci�n de un proceso de Markov
num_pasos = 10
estado_actual = 'A'

print("Secuencia de estados:")
for _ in range(num_pasos):
    # Imprimimos el estado actual seguido de una flecha (->)
    print(estado_actual, end=' -> ')
    
    # Realizamos una transici�n de estado y actualizamos el estado actual
    estado_actual = transicion_estado(estado_actual)

# Imprimimos el �ltimo estado de la secuencia
print(estado_actual)
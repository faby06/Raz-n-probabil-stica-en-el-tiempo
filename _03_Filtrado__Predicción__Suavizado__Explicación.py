import numpy as np

# Definir las matrices del filtro de Kalman
# Estas matrices se simplificar�n en este ejemplo para una serie de tiempo 1D
A = 1  # Matriz de transici�n de estado
H = 1  # Matriz de observaci�n
Q = 0.01  # Covarianza del proceso (ruido del estado)
R = 1  # Covarianza de la medici�n (ruido de la observaci�n)

# Inicializaci�n
estado_predicho = 0  # Supongamos un estado inicial
covarianza_predicha = 1  # Supongamos una covarianza inicial

# Listas para almacenar resultados
estados_filtrados = []
estados_predichos = []

# Datos de la serie de tiempo (simulados)
datos_observados = np.linspace(0, 100, 100)

# Filtro de Kalman
for observacion in datos_observados:
    # Predicci�n del estado
    estado_predicho = A * estado_predicho
    covarianza_predicha = A * covarianza_predicha * A + Q
    
    # Actualizaci�n del estado basada en la observaci�n
    ganancia = covarianza_predicha * H / (H * covarianza_predicha * H + R)
    estado_filtrado = estado_predicho + ganancia * (observacion - H * estado_predicho)
    covarianza_filtrada = (1 - ganancia * H) * covarianza_predicha
    
    # Almacenar resultados
    estados_filtrados.append(estado_filtrado)
    estados_predichos.append(estado_predicho)
    
    # Actualizar el estado predicho para el siguiente paso
    estado_predicho = estado_filtrado
    covarianza_predicha = covarianza_filtrada

# Imprimir resultados
print("Estados filtrados:")
print(estados_filtrados)
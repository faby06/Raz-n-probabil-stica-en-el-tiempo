#Filtros de Kalman
import numpy as np

# Funci�n de transici�n de estado
def transicion_estado(estado_anterior):
    # Simulaci�n de movimiento del objeto
    ruido_transicion = np.random.normal(0, 0.1)  # Ruido de la transici�n
    nuevo_estado = estado_anterior + 1 + ruido_transicion
    return nuevo_estado

# Funci�n de observaci�n
def observacion(estado):
    # Simulaci�n de medici�n
    ruido_observacion = np.random.normal(0, 1)  # Ruido de la observaci�n
    return estado + ruido_observacion

# N�mero de part�culas
num_particulas = 100

# Inicializaci�n de part�culas
particulas = np.random.uniform(0, 1, num_particulas)

# Inicializaci�n de pesos uniformes
pesos = np.ones(num_particulas) / num_particulas

# Datos observados (simulaci�n de mediciones)
observaciones = [3, 4, 5]

# Ciclo principal del filtro de part�culas
for observacion_actual in observaciones:
    # Actualizar las part�culas
    for i in range(num_particulas):
        particulas[i] = transicion_estado(particulas[i])
        prob_observacion = observacion(particulas[i])
        pesos[i] *= np.exp(-0.5 * (observacion_actual - prob_observacion) ** 2)
    
    # Normalizar los pesos
    pesos /= np.sum(pesos)
    
    # Resampling (muestreo de part�culas)
    indices_resample = np.random.choice(np.arange(num_particulas), size=num_particulas, p=pesos)
    particulas = particulas[indices_resample]
    pesos = np.ones(num_particulas) / num_particulas

# Estimaci�n del estado final
estado_estimado = np.mean(particulas)

print("Estado estimado:", estado_estimado)

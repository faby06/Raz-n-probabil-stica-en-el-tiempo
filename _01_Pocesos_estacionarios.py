#Razon. Probabil. en el Tiempo
# Parámetros del proceso AR(1)
phi <- 0.7  # Coeficiente de autoregresión
n <- 100    # Número de observaciones

# Generar un proceso AR(1)
ar1 <- arima.sim(model = list(ar = phi), n = n)

# Crear un objeto de serie temporal
ts_ar1 <- ts(ar1)

# Graficar la serie temporal
plot(ts_ar1, main = "Proceso AR(1)", ylab = "Valor", xlab = "Tiempo")

# Calcular la función de autocorrelación
acf_ar1 <- acf(ts_ar1, plot = FALSE)

# Verificar si la serie es estacionaria
is_stationary <- all(abs(acf_ar1$acf[-1]) < 0.1)
cat("¿Es estacionaria?: ", is_stationary, "\n")

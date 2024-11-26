# Modelo 2: Movimiento de un Péndulo Simple
# Un péndulo simple se mueve bajo la influencia de la gravedad. Su movimiento angular está
# gobernado por la siguiente ecuación diferencial:
# Donde:
# • θ(t) es el ángulo del péndulo respecto a la vertical (en radianes).
# • g = 9.8m/s2
# es la aceleración debida a la gravedad.
# • L es la longitud del hilo del péndulo (en metros).
# Tu tarea es:
# 1. Resolver la ecuación diferencial utilizando el método de Taylor de segundo orden,
# haciendo una aproximación para ángulos pequeños (sin(θ)≈θ).
# 2. Graficar la evolución del ángulo θ(t) en función del tiempo.
# Detalles:
# • Longitud del péndulo: L=2m.
# • Ángulo inicial: 𝜃0=0.2 rad (11.46°).
# • Velocidad angular inicial: dt/dθ (0) = 0 rad/s.
# • Intervalo de tiempo: 𝑡 ∈ [0,10]s.
# • Tamaño del paso: h = 0.1s.
# Requerimientos del programa:
# 1. Implementar el método de Taylor de segundo orden para resolver el sistema de
# ecuaciones:
# donde 𝜔 = dt/dθ es la velocidad angular.
# 2. Graficar los resultados:
# a. La evolución del ángulo θ(t) en función del tiempo.
# b. Opcional: la evolución de la velocidad angular 𝜔 = (t).


import numpy as np
import matplotlib.pyplot as plt

# Parámetros
longitud = 2.0  # Longitud del péndulo (m)
gravedad = 9.8  # Aceleración de la gravedad (m/s²)
angulo_inicial = 0.2  # Ángulo inicial (rad)
velocidad_inicial = 0  # Velocidad angular inicial (rad/s)
tiempo_inicial = 0  # Tiempo inicial (s)
tiempo_final = 10  # Tiempo final (s)
h = 0.1  # Paso de tiempo (s)

# Calcular número de pasos
n = int((tiempo_final - tiempo_inicial) / h)

# Inicializar arreglos
tiempo = np.linspace(tiempo_inicial, tiempo_final, n+1)
angulo = np.zeros(n+1)
velocidad_angular = np.zeros(n+1)

# Condiciones iniciales
angulo[0] = angulo_inicial
velocidad_angular[0] = velocidad_inicial

# Primeras derivadas
def derivada_angulo(vel):
    return vel

def derivada_velocidad(ang):
    return -(gravedad/longitud) * ang  # Aproximación para ángulos pequeños: sin(θ) ≈ θ

# Segundas derivadas
def segunda_derivada_angulo(ang):
    return derivada_velocidad(ang)

def segunda_derivada_velocidad(vel):
    return -(gravedad/longitud) * vel

# Método de Taylor de segundo orden
for i in range(n):
    angulo[i+1] = angulo[i] + h*derivada_angulo(velocidad_angular[i]) + \
                  (h**2/2)*segunda_derivada_angulo(angulo[i])
    velocidad_angular[i+1] = velocidad_angular[i] + h*derivada_velocidad(angulo[i]) + \
                            (h**2/2)*segunda_derivada_velocidad(velocidad_angular[i])

# Gráficas
plt.figure(figsize=(12, 8))

# Gráfica del ángulo vs tiempo
plt.subplot(2, 1, 1)
plt.plot(tiempo, angulo, 'b-', label='θ(t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ángulo (rad)')
plt.title('Movimiento del Péndulo - Ángulo vs Tiempo')
plt.grid(True)
plt.legend()

# Gráfica de la velocidad angular vs tiempo
plt.subplot(2, 1, 2)
plt.plot(tiempo, velocidad_angular, 'r-', label='ω(t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad Angular (rad/s)')
plt.title('Movimiento del Péndulo - Velocidad Angular vs Tiempo')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()


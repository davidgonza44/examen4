import matplotlib.pyplot as plt
from modelos.modelo_enfriamiento import ModeloEnfriamiento
from modelos.modelo_pendulo import ModeloPendulo

def graficar_enfriamiento():
    modelo = ModeloEnfriamiento()
    tiempo, temperatura = modelo.calcular_enfriamiento()

    plt.figure(figsize=(10, 6))
    plt.plot(tiempo, temperatura, 'b-', label='Temperatura del café')
    plt.axhline(y=modelo.temp_ambiente, color='r', linestyle='--',
                label='Temperatura ambiente')
    plt.xlabel('Tiempo (minutos)')
    plt.ylabel('Temperatura (°C)')
    plt.title('Simulación del Enfriamiento del Café')
    plt.grid(True)
    plt.legend()
    plt.show()

def graficar_pendulo():
    modelo = ModeloPendulo()
    tiempo, angulo, velocidad = modelo.calcular_movimiento()

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 1, 1)
    plt.plot(tiempo, angulo, 'b-', label='θ(t)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Ángulo (rad)')
    plt.title('Movimiento del Péndulo - Ángulo vs Tiempo')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(tiempo, velocidad, 'r-', label='ω(t)')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad Angular (rad/s)')
    plt.title('Movimiento del Péndulo - Velocidad Angular vs Tiempo')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

pregunta = input("¿Desea graficar el modelo de enfriamiento del café o el modelo del péndulo? (enfriamiento/pendulo): ")
if pregunta.lower() == "enfriamiento":
    graficar_enfriamiento()
elif pregunta.lower() == "pendulo":
    graficar_pendulo()
else:
    print("Opción no válida. Por favor, seleccione 'enfriamiento' o 'pendulo'.")
    exit()

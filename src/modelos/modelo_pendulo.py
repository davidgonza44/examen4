import numpy as np

class ModeloPendulo:
    def __init__(self, longitud=2.0, gravedad=9.8, angulo_inicial=0.2,
                 velocidad_inicial=0, tiempo_inicial=0, tiempo_final=10, h=0.1):
        if not isinstance(angulo_inicial, (int, float)):
            raise ValueError("El ángulo inicial debe ser un número")
        self.longitud = float(longitud)
        self.gravedad = float(gravedad)
        self.h = h
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final

        self.n = int((tiempo_final - tiempo_inicial) / h)
        self.tiempo = np.linspace(tiempo_inicial, tiempo_final, self.n+1)
        self.angulo_inicial = np.zeros(self.n+1)
        self.velocidad_angular = np.zeros(self.n+1)

        self.angulo_inicial[0] = float(angulo_inicial)
        self.velocidad_angular[0] = float(velocidad_inicial)

    def derivada_angulo(self, vel):
        return vel

    def derivada_velocidad(self, ang):
        return -(self.gravedad/self.longitud) * ang

    def segunda_derivada_angulo(self, ang):
        return self.derivada_velocidad(ang)

    def segunda_derivada_velocidad(self, vel):
        return -(self.gravedad/self.longitud) * vel

    def calcular_movimiento(self):
        for i in range(self.n):
            self.angulo_inicial[i+1] = (self.angulo_inicial[i] +
                               self.h * self.derivada_angulo(self.velocidad_angular[i]) +
                               (self.h**2/2) * self.segunda_derivada_angulo(self.angulo_inicial[i]))

            self.velocidad_angular[i+1] = (self.velocidad_angular[i] +
                                         self.h * self.derivada_velocidad(self.angulo_inicial[i]) +
                                         (self.h**2/2) * self.segunda_derivada_velocidad(self.velocidad_angular[i]))

        return self.tiempo, self.angulo_inicial, self.velocidad_angular

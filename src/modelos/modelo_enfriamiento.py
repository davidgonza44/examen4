import numpy as np

class ModeloEnfriamiento:
    def __init__(self, temp_inicial=90, temp_ambiente=25, k=0.1,
                 tiempo_inicial=0, tiempo_final=60, h=5):

        self.temp_inicial = float(temp_inicial)
        self.temp_ambiente = float(temp_ambiente)
        self.k = float(k)
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final
        self.h = h
        self.n = int((tiempo_final - tiempo_inicial) / h)

        self.tiempo = np.linspace(tiempo_inicial, tiempo_final, self.n+1)
        self.temperatura = np.zeros(self.n+1)
        self.temperatura[0] = temp_inicial

    def derivada_temp(self, temp):
        return -self.k * (temp - self.temp_ambiente)

    def segunda_derivada_temp(self, temp):
        return -self.k * self.derivada_temp(temp)

    def calcular_enfriamiento(self):
        for i in range(self.n):
            self.temperatura[i+1] = (self.temperatura[i] +
                                   self.h * self.derivada_temp(self.temperatura[i]) +
                                   (self.h**2/2) * self.segunda_derivada_temp(self.temperatura[i]))
        return self.tiempo, self.temperatura

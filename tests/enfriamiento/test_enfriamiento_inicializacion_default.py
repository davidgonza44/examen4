import unittest
import numpy as np
from src.modelos.modelo_enfriamiento import ModeloEnfriamiento

class TestModeloEnfriamiento(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para cada prueba"""
        self.modelo = ModeloEnfriamiento()

    def test_temperatura_inicial(self):
        """Verifica que la temperatura inicial sea correcta"""
        tiempo, temp = self.modelo.calcular_enfriamiento()
        self.assertEqual(temp[0], 90)

    def test_temperatura_decrece(self):
        """Verifica que la temperatura siempre decrece"""
        tiempo, temp = self.modelo.calcular_enfriamiento()
        for i in range(1, len(temp)):
            self.assertTrue(temp[i] < temp[i-1])

    def test_temperatura_final_cercana_ambiente(self):
        """Verifica que la temperatura final se acerca a la ambiente"""
        tiempo, temp = self.modelo.calcular_enfriamiento()
        self.assertLess(abs(temp[-1] - self.modelo.temp_ambiente), 10)

    def test_derivada_temp(self):
        """Verifica que la derivada de temperatura sea correcta"""
        derivada = self.modelo.derivada_temp(90)
        valor_esperado = -self.modelo.k * (90 - self.modelo.temp_ambiente)
        self.assertAlmostEqual(derivada, valor_esperado)

if __name__ == '__main__':
    unittest.main()

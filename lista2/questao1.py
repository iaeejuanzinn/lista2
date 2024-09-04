import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

circulo = Circulo(5)
print(f"A área do círculo é: {circulo.calcular_area()}")  

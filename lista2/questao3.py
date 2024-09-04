class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# Exemplo de uso
retangulo = Retangulo(4, 6)
print(f"A área do retângulo é: {retangulo.calcular_area()}")  # Saída: A área do retângulo é: 24

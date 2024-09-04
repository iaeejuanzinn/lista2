class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade


produto = Produto("Laptop", 3000.00, 2)
total = produto.calcular_total()
print(f"Valor total do produto: R${total:.2f}") 

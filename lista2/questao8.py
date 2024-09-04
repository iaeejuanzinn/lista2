class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if not self.notas: 
            return 0
        return sum(self.notas) / len(self.notas)


aluno = Aluno("Carlos", [7.5, 8.0, 9.0, 6.5])
media = aluno.calcular_media()
print(f"A média das notas de {aluno.nome} é: {media:.2f}") 

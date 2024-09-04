class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual):
        if percentual > 0:
            aumento = self.salario * (percentual / 100)
            self.salario += aumento
            print(f"Salário aumentado em {percentual}% para R${self.salario:.2f}.")
        else:
            print("O percentual de aumento deve ser positivo.")


funcionario = Funcionario("Ana", 3000.00, "Analista")
print(f"Salário inicial: R${funcionario.salario:.2f}")

funcionario.aumentar_salario(10)  
print(f"Salário após aumento: R${funcionario.salario:.2f}")

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def consultar_saldo(self):
        return self.saldo


conta = ContaBancaria("João", 1000)
print(f"Saldo inicial: R${conta.consultar_saldo():.2f}")

conta.depositar(500)
print(f"Saldo após depósito: R${conta.consultar_saldo():.2f}")

conta.sacar(300)
print(f"Saldo após saque: R${conta.consultar_saldo():.2f}")

conta.sacar(1500)  

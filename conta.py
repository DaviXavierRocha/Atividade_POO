class Conta:
    def __init__(self, numeroconta, titular, saldo, limite):
        self.numeroconta = numeroconta
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'Olá Sr {self.titular}!\nSeu Saldo é de R$ {self.saldo}\nSeu limite é de: R$ {self.limite}')  

    def depositar(self, valor):
        self.saldo += valor

    def saque(self, valor):
            self.saldo -= valor


conta1=Conta('4328-1', 'Davi Rocha', 250, 600)
conta1.extrato()
conta1.depositar(50)
conta1.saque(100)
conta1.extrato()
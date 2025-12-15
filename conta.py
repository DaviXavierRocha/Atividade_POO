from cliente import Cliente

class Conta:
    def __init__(self, numeroconta, saldo, limite, nome, cpf, dia_nasc, mes_nasc, ano_nasc, telefone, email, logradouro, bairro, numero, cidade, estado, cep, complemento):
        self.numeroconta = numeroconta
        self.titular = Cliente(nome, cpf, dia_nasc, mes_nasc, ano_nasc, telefone, email, logradouro, bairro, numero, cidade, estado, cep, complemento)
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(20*'*')
        print(f'Olá Sr(a) {self.titular.nome}!\nSeu Saldo é de R$ {self.saldo}\nSeu limite é de: R$ {self.limite}')

    def depositar(self, valor):
        self.saldo += valor
        print(20*'*')
        print(f'Valor de {valor} depositado na conta de {self.titular.nome}')

    def saque(self, valor):
        self.saldo -= valor
        print(20*'*')
        print(f'Valor de {valor} sacado na conta de {self.titular.nome}')

    def transferir(self, valor, Conta_Dest): #transferencia, pede uma conta de destino
        self.saque(valor)
        Conta_Dest.depositar(valor)
        Conta_Dest.extrato()
        self.extrato()
        print(20*'*')
        print(f'Transferencia de R$ {valor} feita do(a) titular {self.titular.nome} para o(a) titular {Conta_Dest.titular.nome}')
        print(20*'*')
#Ele imprime os extratos no proprio metodo, achei mais conveniente para testar

conta1 = Conta(
    numeroconta=12345,
    saldo=1500.00,
    limite=500.00,
    nome="João da Silva",
    cpf="123.456.789-00",
    dia_nasc=15,
    mes_nasc=5,
    ano_nasc=1990,
    telefone="(11) 98765-4321",
    email="joao.silva@email.com",
    logradouro="Rua das Flores",
    bairro="Centro",
    numero='100',
    cidade="São Paulo",
    estado="SP",
    cep="01001-000",
    complemento="Apto 101"
)

conta2= Conta(
    numeroconta=88002,
    saldo=250.50,
    limite=1000.00,
    nome="Maria Oliveira",
    cpf="987.654.321-11",
    dia_nasc=20,
    mes_nasc=10,
    ano_nasc=1985,
    telefone="(21) 91234-5678",
    email="maria.oliveira@email.com",
    logradouro="Av. Atlântica",
    bairro="Copacabana",
    numero='400',
    cidade="Rio de Janeiro",
    estado="RJ",
    cep="22000-000",
    complemento="Bloco B, Ap 50"
)
conta1.extrato()
conta2.extrato()
conta1.transferir(20, conta2)



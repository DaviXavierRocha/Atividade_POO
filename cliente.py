from endereco import Endereco
class Cliente:
    def __init__(self, nome, cpf, data_nasc, telefone, email, logradouro, bairro, numero, cep, complemento):
        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.telefone = telefone
        self.email = email
        self.endereco = Endereco(logradouro, bairro, numero, cep, complemento)


class Endereco:
    def __init__(self, logradouro, bairro, numero, cidade, estado, cep, complemento='sem complemento'):
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.complemento = complemento

        # Precisa de validação:
        self.estado = estado
        self.cep = cep
        self.numero = numero

        def verificador_estado(self, estado):
            estado = estado.strip().upper() #strip remove os espaços e upper torna tudo maiusculo
            if len(estado) != 2 or not estado.isalpha():
                raise ValueError("O estado deve conter exatamente 2 letras")
            self.estado = estado

        def verificador_cep(self, cep):
            cep= cep.strip().replace("-","") #remove o hifen (ou so substitui por nada)
            if len(cep) != 8 or not cep.isdigit():
                raise ValueError("O CEP deve conter exatamente 8 números")
            self.cep = cep # nesse caso optei usar o salvamento sem hifen mesmo
        
        def verificador_numero(self, numero):
            if numero.isdigit() == False:
                raise ValueError('Aí voce ta de brincadeira')
            self.numero = numero

        verificador_estado(self, estado)
        verificador_cep(self, cep)
        verificador_numero(self, numero)

    def __str__(self):
        return f"{self.logradouro}, {self.numero}, {self.bairro}, {self.cep}, {self.cidade} - {self.estado}"

    def trocar_endereco_completo(self):
        print('Mudando seu endereço: ')
        self.logradouro = input('Digite seu logradouro: ')
        self.bairro = input('Digite seu Bairro: ')
        self.numero = input('Digite seu Numero: ')
        self.complemento = input('Digite seu Complemento: ')
        self.cep = (input('Digite seu Cep: '))
        self.estado(input("Digite seu estado: "))
        self.cidade = input('Digite sua Cidade: ')

    def trocar_endereco_parcial(self, operador):
        if operador == 1:
            self.logradouro = input('Digite seu logradouro: ')
        elif operador == 2:
            self.bairro = input('Digite seu Bairro: ')
        elif operador == 3:
            self.numero = input('Digite seu Numero: ')
        elif operador == 4:
            self.complemento = input('Digite seu Complemento: ')
        elif operador ==5:
            self.cep = (input('Digite seu Cep: '))
        elif operador == 6:
            self.estado(input("Digite seu estado: "))
        elif operador == 7:
            self.cidade = input('Digite sua Cidade: ')
        else:
            print("Saindo")




#endereco1=Endereco('Rua maceio', 'Dom Lustosa', '72', 'Fortaleza', 'CE', '12345678')
#print(endereco1)

#endereco1.trocar_endereco()


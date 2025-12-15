from endereco import Endereco
class Cliente:
    def __init__(self, nome, cpf, dia_nasc, mes_nasc, ano_nasc, telefone, email, logradouro, bairro, numero, cidade, estado, cep, complemento):
        self.nome = nome
        self.endereco = Endereco(logradouro, bairro, numero, cidade, estado, cep, complemento)
        
        # Necessitam de Validação
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.dia_nasc = dia_nasc
        self.mes_nasc = mes_nasc
        self.ano_nasc = ano_nasc

        def validar_dia(dia_nasc):
            if dia_nasc > 0 and dia_nasc < 32:
                #print("valor válido")
                return True
            else:
                #print("valor inválido")
                return False
            
        def validar_mes(mes_nasc):
            if mes_nasc > 0 and mes_nasc < 13:
                #print("valor válido")
                return True
            else:
                #print("valor inválido")
                return False
        
        def validar_ano(ano_nasc):
            if ano_nasc < 1900 and ano_nasc < 2026:
                #print("valor válido")
                return True
            else:
                #print("valor inválido")
                return False
            
        def data_nasc(dia_nasc, mes_nasc, ano_nasc):
            if validar_dia(dia_nasc) == False and validar_mes(mes_nasc) == False and validar_ano(ano_nasc) == False:
                raise ValueError('data errada, forneça valores válidos maiores que 0 e menores que 32 para dia, menor que 13 para mes e maior que 1905 para o ano e menor que 2026')
                        
            self.dia_nasc = dia_nasc
            self.mes_nasc = mes_nasc
            self.ano_nasc = ano_nasc
            return f"{dia_nasc}/{mes_nasc}/{ano_nasc}"

        def validar_CPF(cpf):
            cpf = cpf.strip().replace("-","") #Retira os -
            cpf = cpf.strip().replace(".","") #Retira os pontos
            if len(cpf) != 11 and not cpf.isdigit(): #Verifica tamanho e se há letra
                raise ValueError('CPF inválido digite somente numeros')
            else:
                self.cpf = cpf #caso seja valido
        
        def validar_email(email):
            if '@' and '.com' in email: #verifica se o email tem @ e .com
                self.email = email
            else:
                raise ValueError('Email inválido, favor digitar um email valido exemplo: aaaaa@dominio.com')
            return email
        
        def validar_telefone(telefone):
            telefone = telefone.strip().replace("-","")#retira hifens, parenteses e espaços
            telefone = telefone.strip().replace("(","")
            telefone = telefone.strip().replace(")","")
            telefone = telefone.strip().replace(" ","")
            if not telefone.isdigit() or len(telefone) != 11:
                raise ValueError('telefone inválido')
            else:
                self.telefone = telefone
            


        data_nasc(dia_nasc, mes_nasc, ano_nasc)
        validar_CPF(cpf)
        validar_email(email)
        validar_telefone(telefone)
    
    def trocar_endereço(self):
        operador = int(input('Digite 1 para trocar parcialmente o endereço, 2 para trocar completamente o endereço e 3 para sair\n'))
        if operador == 3:
            print('Saindo')
        elif operador == 2:
            self.endereco.trocar_endereco_completo()
        elif operador == 1:
            operadorParcial = int(input("Digite o que deseja mudar:\n1) Logradouro\n2) Bairro\n3) Numero\n4) Complemento\n5) CEP\n6) Estado\n7) Cidade\n8) Sair\n"))
            self.endereco.trocar_endereco_parcial(operadorParcial)
        else:
            raise ValueError("Operação Inválida")
        print(self.endereco)

    def __str__(self):
        return f'Nome: {self.nome}, CPF: {self.cpf}'
    


cliente1 = Cliente(nome="João Silva", cpf="12345678901", dia_nasc=15, mes_nasc=8, ano_nasc=1990, telefone="(11) 98765-4321", email="joao.silva@gmail.com", logradouro="Rua das Flores", bairro="Centro", numero="123", cidade="São Paulo", estado="SP", cep="01001-000", complemento="Apto 45")
cliente1.trocar_endereço()
#print(cliente_teste.data_nasc())
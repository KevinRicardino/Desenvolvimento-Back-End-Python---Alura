'''
Criando classes, construtores e métodos:

Crie um método de classe para a conta ClienteBanco.
'''

class ClienteBanco:
    clientes = [] # Lista de clientes armazenados

    def __init__(self, nome, cidade, cpf, profissao, telefone):
        self._nome = nome.title()
        self._cidade = cidade.title()
        self._cpf = cpf
        self._profissao = profissao
        self._telefone = telefone
        ClienteBanco.clientes.append(self) # Adiciona cada cliente criado à lista

    @classmethod
    def listar_clientes(cls):
        print('Relação dos Clientes')
        for cliente in cls.clientes:
            print(
                f'Nome: {cliente._nome}\n'
                f'Cidade: {cliente._cidade}\n'
                f'cpf: {cliente._cpf}\n'
                f'Profissão: {cliente._profissao}\n'
                f'Telefone: {cliente._telefone}\n'
                + '-'* 20
            )

# Criando clientes
cliente1 = ClienteBanco('Kamala', 'Manaus', 59614376040, 'Veterinaria', 11111-222)
cliente2 = ClienteBanco('Juliana', 'Fortaleza', 96703580006, 'Medica', 85467-986)
cliente3 = ClienteBanco('Amanda', 'Natal', 42346760048, 'Engenheira', 85721-457)

# Listando todos os clientes
ClienteBanco.listar_clientes()
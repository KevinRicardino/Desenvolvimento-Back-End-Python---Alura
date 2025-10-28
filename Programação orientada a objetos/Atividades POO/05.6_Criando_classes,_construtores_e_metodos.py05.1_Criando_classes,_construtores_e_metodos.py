'''
Criando classes, construtores e métodos:

Crie uma classe chamada ClienteBanco com um construtor 
que aceita 5 atributos. Instancie 3 objetos desta classe 
e atribua valores aos seus atributos através do método 
construtor.
'''

class ClienteBanco:
    def __init__(self, nome, cidade, cpf, profissao, telefone):
        self._nome = nome.title()
        self._cidade = cidade.title()
        self._cpf = cpf
        self._profissao = profissao
        self._telefone = telefone

cliente1 = ClienteBanco('Kamala', 'Manaus', 59614376040, 'Veterinaria', 11111-222)
cliente2 = ClienteBanco('Juliana', 'Fortaleza', 96703580006, 'Medica', 85467-986)
cliente3 = ClienteBanco('Amanda', 'Natal', 42346760048, 'Engenheira', 85721-457)
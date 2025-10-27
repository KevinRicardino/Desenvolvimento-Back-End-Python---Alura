'''
Métodos especiais e atributos:

Modifique a classe Restaurante adicionando um construtor que aceita nome 
e categoria como parâmetros e inicia ativo como False por padrão. Crie uma 
instância utilizando o construtor.
'''

class Restaurante:

    def __init__(self, nome, categoria, endereco, capacidade, ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.endereco = endereco
        self.capacidade = capacidade

    def __str__(self):
        return f' → {self.nome} | {self.categoria} | {self.ativo} | {self.endereco} | {self.capacidade}'
    
restaurante_churrasco = Restaurante('Carne de Panela', 'carnes', 'Varginha', '15')

print(restaurante_churrasco)
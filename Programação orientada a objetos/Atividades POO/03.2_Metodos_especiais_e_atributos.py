'''
Métodos especiais e atributos:

Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie 
mais 2 atributos.Instancie um restaurante e atribua valores aos seus atributos.
'''

class Restaurante:

    def __init__(self, nome, categoria, endereco, capacidade):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.endereco = endereco
        self.capacidade = capacidade

    def __str__(self):
        return f' → {self.nome} | {self.categoria} | {self.ativo} | {self.endereco} | {self.capacidade}'
    
restaurante_churrasco = Restaurante('Carne de Panela', 'carnes', 'Varginha', '15')

print(restaurante_churrasco)
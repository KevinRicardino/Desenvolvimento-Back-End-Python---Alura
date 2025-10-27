'''
Métodos especiais e atributos:

Adicione um método especial __str__ à classe Restaurante para que, ao imprimir 
uma instância, seja exibida uma mensagem formatada com o nome e a categoria. 
Exiba essa mensagem para uma instância de restaurante.
'''

class Restaurante:

    def __init__(self, nome, categoria, endereco, capacidade, ativo = False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.endereco = endereco
        self.capacidade = capacidade

    def __str__(self):
        return (
         
        f" → O restaurante '{self.nome}' pertence à categoria '{self.categoria}' "
        f"e possui status '{self.ativo}', localizado em '{self.endereco}' "
        f"com capacidade para '{self.capacidade}' pessoas."

        )

restaurante_churrasco = Restaurante('Carne de Panela', 'carnes', 'Varginha', '15')

print(restaurante_churrasco)
'''
Refatorando uma função:

A criação de classes em Python é uma maneira poderosa de estruturar código de forma orientada a objetos. 
Abaixo, temos um exemplo de uma classe chamada Livro que representa informações sobre um livro, como 
título, autor e número de páginas:

    class Livro:
        def __init__(self, titulo='', autor='', paginas=0):
            self.titulo = titulo
            self.autor = autor
            self.paginas = paginas

        def __str__(self):
            return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

        @property
        def titulo_autor(self):
            return f'{self.titulo} por {self.autor}'

        def aumentar_paginas(self, quantidade):
            self.paginas += quantidade

Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. 
Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente 
também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, 
adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com 
base na profissão da pessoa.
'''

# Definição da classe Pessoa
# Essa classe representa uma pessoa com nome, idade e profissão
class Pessoa:

    # Método construtor (__init__)
    # É chamado automaticamente quando criamos um novo objeto da classe
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome            # Atributo que armazena o nome da pessoa
        self.idade = idade          # Atributo que armazena a idade da pessoa
        self.profissao = profissao  # Atributo que armazena a profissão da pessoa

    # Método especial __str__
    # Define como o objeto será exibido quando usamos print() ou str()
    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}.'
    
    # Método de instância aniversario()
    # Aumenta a idade da pessoa em 1 quando é chamado
    def aniversario(self):
        self.idade += 1

    # Propriedade saudacao
    # Usando @property, podemos acessar esse método como se fosse um atributo
    @property
    def saudacao(self):
        # Retorna uma mensagem de saudação personalizada
        return f'Olá! Meu nome é {self.nome} e eu trabalho com {self.profissao}.'
    
# -------------------- EXEMPLO DE USO --------------------

# Cria um objeto de classe Pessoa com nome, idade e profissão
pessoa1 = Pessoa('Maria', 28, 'Engenheira')

# Exibe as informações da pessoa (usa o método __str__)
print(pessoa1)              # Saída: Maria, 28 anos, Engenheira

# Exibe a saudação personalizada (usa a propriedade saudacao)
print(pessoa1.saudacao)     # Saída: Olá! Meu nome é Maria e eu trabalho como Engenheira.

# Chama o método aniversario(), aumentando a idade em 1
pessoa1.aniversario()

# Exibe novamente as informações, agora com a idade atualizada
print(pessoa1)              # Saída: Maria, 29 anos, Engenheira
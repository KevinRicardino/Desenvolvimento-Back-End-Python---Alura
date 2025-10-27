'''
Classe música:

Em programação orientada a objetos (OO), uma classe é um modelo para criar objetos. 
Um objeto é uma instância específica de uma classe, e as classes são utilizadas para 
definir o comportamento e as propriedades compartilhadas por um grupo de objetos relacionados.

Por exemplo, uma classe Música poderia ter 3 atributos (que trazem as características ou propriedades de um objeto):

    nome
    artista
    duracao

Agora é sua vez! Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo..
'''

class Musica:
    '''
    Classe que representa uma música.
    Possui três atributos:
    - nome
    - artista
    - duração (em minutos)
    '''
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def exibir_informacoes(self):
        '''
        Exibe as informações da música formatadas.
        '''
        print(f'Música: {self.nome}')
        print(f'Artista: {self.artista}')
        print(f'Duração: {self.duracao} min\n')

def main():
    print('=== Cadastro de Músicas ===\n')

    # Criando 3 objetos da classe Musica
    musica1 = Musica('Fix You', 'Coldplay', 5.07)
    musica2 = Musica('Billie Jean', 'Michael Jackson', 4.54)
    musica3 = Musica('Bohemian Rhapsody', 'Queen', 5.55)

    # Exibindo informações das músicas
    print('=== Lista de Músicas Cadastradas ===\n')
    musica1.exibir_informacoes()
    musica2.exibir_informacoes()
    musica3.exibir_informacoes()    

if __name__ == '__main__':
    main()
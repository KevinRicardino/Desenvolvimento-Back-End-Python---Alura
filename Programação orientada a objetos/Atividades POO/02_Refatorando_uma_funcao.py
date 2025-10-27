'''
Refatorando uma função:

No Python, a criação de classes é uma parte essencial da programação orientada 
a objetos. Abaixo, temos um exemplo de uma classe chamada Musica que representa 
informações sobre uma música, como nome, artista e duração:

    class Musica:
        nome = ''
        artista = ''
        duracao = int

Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, 
aproveitando a sintaxe simplificada do Python.  
'''

# Classe que representa uma música
class Musica:
    
    # Lista de todas as músicas criadas
    musicas = [] 

    def __init__(self, nome, artista, duracao):
        '''
        Construtor da classe Musica.
        Recebe o nome, o artista e a duração da música.
        '''
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self) # Adiciona automaticamente à lista geral

    def __str__(self):
        '''
        Retorna uma representação amigável da música. 
        ''' 
        return f'{self.nome} | {self.artista}'
    
    @staticmethod
    def listar_musicas():
        '''
        Exibe todas as músicas cadastradas, com seus detalhes.
        '''
        print('Lista de músicas cadastradas:')
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao} min')

# Criação de objetos da classe Musica
musica1 = Musica('Love of My Life', 'Queen', 6.2)
musica2 = Musica('Yesterday', 'The Beatles', 4.6)

# Chamada do método que lista todas as músicas
Musica.listar_musicas()
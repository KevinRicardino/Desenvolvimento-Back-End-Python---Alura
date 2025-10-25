'''
Encontrando palavras que começam com uma letra específica:

Você trabalha em uma biblioteca e está organizando os títulos de livros 
no sistema. Você precisa identificar todos os títulos que possuem palavras 
iniciadas por uma determinada letra, para criar coleções temáticas baseadas 
em letras específicas. Por exemplo, você poderia usar isso para agrupar 
livros com palavras que começam com a mesma letra, ajudando na organização 
ou em campanhas como “Livros com A para você!”.

Como você criaria um programa que solicita um texto e uma letra inicial e 
retorna todas as palavras do texto que começam com essa letra?

Exemplo de Entrada:

    Digite o título dos livro: As Aventuras de Alice no País das Maravilhas Digite a letra inicial para pesquisa: A

Saída esperada:

    ["As", "Aventuras", "Alice"]
'''

import re

def encontrar_palavras_iniciais():
    '''Encontra palavras em um texto que começam com uma letra específica.'''

    # Solicita o texto do usuário
    texto = input('Digite o título dos livros: ')
    letra_inicial = input('Digite a letra inicial para pesquisa: ')

    # Cria o padrão regex para encontrar palavras que começam com a letra específicada
    # O \b indica limite de palavra, re.IGNORECASE torna a pesquisa insensível a maiúsculas/minúsculas
    padrao = rf'\b{re.escape(letra_inicial)}\w*'

    # Usa findall para encontrar todas as correspondências
    palavras_encontradas = re.findall(padrao, texto, re.IGNORECASE)

    print(palavras_encontradas)

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == "__main__":
    encontrar_palavras_iniciais()
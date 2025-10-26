'''
Cadastro de Produtos:

Ana é responsável pelo controle de estoque de uma loja de artigos para papelaria. 
Ela precisa de um programa que permita cadastrar produtos em forma de dados estruturados. 
O sistema deve solicitar o nome e a quantidade de três produtos e, ao final, exibir as informações 
cadastradas em um dicionário, onde cada produto será uma chave e a quantidade correspondente será o valor.

Exemplo de entrada:

    Digite o nome do produto: Caneta 
    Digite a quantidade: 50
    Digite o nome do produto: Caderno 
    Digite a quantidade: 30 
    Digite o nome do produto: Borracha 
    Digite a quantidade: 20 

Saída esperada:

    Dicionário de produtos: {'Caneta': 50, 'Caderno': 30, 'Borracha': 20} 
'''
import re

def nome_valido(nome_produto):
    '''Verifica se o nome do produto possui apenas letras e espaços.'''

    return re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?: [A-Za-zÀ-ÖØ-öø-ÿ]+)*", nome_produto) is not None # <ALT> + 0216 = Ø | <ALT> + 0248 = ø | <ALT> + 26 = →

def quantidade_valida(valor):
    '''Verifica se o valor digitado é um número inteiro positivo.'''
    return valor.isdigit() and int(valor) >= 0

def obter_produto():
    '''
    Solicita ao usuário o nome e a quantidade de um produto,
    garantindo que as entradas sejam válidas.
    Retorna uma tupla (nome, quantidade).
    '''
    while True:
        nome_produto = input('Digite o nome do produto: ').strip().title()

        if not nome_valido(nome_produto):
            print('Nome inválido. Digite apenas letras e espaços. Não use números ou símbolos.')
            continue

        quantidade = input('Digite a quantidade: ').strip()

        if not quantidade_valida(quantidade):
            print('Quantidade inválida. Digite um número inteiro positivo.')
            continue

        return nome_produto, int(quantidade)
    


def main():
    '''
    Função principal que cadastra três produtos e exibe o diiconário final.
    '''

    produtos = {} # Dicionário vazio

    print('\n=== Cadastro de Produtos ===\n')

    for _ in range(3):
        nome, quantidade = obter_produto()
        produtos[nome] = quantidade
        print(f'O produto "{nome}" com quantidade {quantidade} foi cadastrado com sucesso!\n')

    print(f'Dicionário de produtos: {produtos}')

# Executa a função apenas se o arquivo for chamado diretamente
if __name__ == '__main__':
    main()
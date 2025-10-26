'''
Atualizando informações no estoque:

Ana percebeu que, após o cadastro inicial dos produtos, precisa 
atualizar a quantidade de um item específico no estoque. Sua tarefa 
é criar um programa que solicite o nome do produto e a nova quantidade, 
atualizando essa informação no dicionário de estoque.

Exemplo de entrada:

    estoque = { 

        "Caderno universitário": 50, 
        "Caneta azul": 120, 
        "Borracha branca": 30 

    } 

    Nome do produto a ser atualizado: Caneta azul 
    Nova quantidade: 150 

Saída esperada:

    { 

        "Caderno universitário": 50, 

        "Caneta azul": 150, 

        "Borracha branca": 30 

    } 
'''

import re

def nome_valido(nome_produto):
    '''
    Verifica se o nome do produto possui apenas letras e espaços.
    Aceita caracteres acentuados.
    '''

    return re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?: [A-Za-zÀ-ÖØ-öø-ÿ]+)*", nome_produto) is not None # Obs: Ø = ALT+0216 | ø = ALT+0248 | → = ALT+26

def quantidade_valida(valor):
    '''
    Verifica se o valor digitado é um número inteiro positivo.
    '''
    return valor.isdigit() and int(valor) >= 0

def atualizar_estoque(estoque):
    '''
    Solicita o nome de um produto e a nova quantidade.
    Atualiza o dicionário de estoque, se o produto existir.
    '''
    nome_produto = input('Digite o nome do produto a ser atualizado: ').strip()

    # Verifica se o nome é válido
    if not nome_valido(nome_produto):
        print('Nome inválido. Digite apenas letras e espaços.')
        return
    
    # Localiza o produto ignorando acentuação e caixa
    produto_encontrado = None
    for produto in estoque:
        if produto.casefold() == nome_produto.casefold():
            produto_encontrado = produto
            break

    if not produto_encontrado:
        print(f'O produto "{nome_produto}" não foi encontrado no estoque.')
        return
    
    # Solicita nova quantidade
    nova_quantidade = input(f'Digite a nova quantidade para "{produto_encontrado}": ').strip()

    if not quantidade_valida(nova_quantidade):
        print('Quantidade inválida. Digite um número inteiro positivo.')
        return
    
    # Atualiza o dicionário
    estoque[produto_encontrado] = int(nova_quantidade)
    print(f'A quantidade do produto "{produto_encontrado}" foi atualizada para {nova_quantidade}.')

def main():
    '''
    Função principal: define o estoque inicial e permite atualização.
    '''
    estoque = {
        "Caderno universitário": 50,
        "Caneta azul": 120,
        "Borracha branca": 30
    }

    print('\n=== Atualização de Estoque ===\n')

    atualizar_estoque(estoque)

    print('\nEstoque atualizado:')
    print(estoque)

# Executa a função apenas se o arquivo for chamado diretamente
if __name__ == '__main__':
    main()
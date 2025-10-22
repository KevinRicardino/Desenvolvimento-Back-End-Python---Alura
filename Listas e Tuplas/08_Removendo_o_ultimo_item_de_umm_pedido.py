'''
Removendo o último item de um pedido:

Paulo está criando uma lista de pedidos para a lanchonete. Ele já tem todos 
os pedidos, mas percebeu que o último foi inserido por engano e precisa removê-lo.

Diante deste problema, ajude Paulo criando um programa que automatize essa 
operação, permitindo listar os pedidos e remover o último item automaticamente.

Exemplo de Entrada:

    Pedidos feitos (separados por vírgula): Sanduíche, Suco, Sobremesa

Saída esperada: 

    Pedidos finais: ['Sanduíche', 'Suco']
'''

def remover_ultimo_pedido():
    '''Lê uma lista de pedidos e remove automaticamente o último item.'''

    # Entrada dos pedidos feita pelo usuário
    entrada = input('Pedidos feitos (separados por vírgula): ')

    # Converte a entrada em lista, removendo espaços extras
    pedidos = [item.strip() for item in entrada.split(',')]

    # Remove o último pedido da lista
    if pedidos:
        pedidos.pop()

    # Exibe a lista final
    print(f'\nPedidos finais: {pedidos}')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    remover_ultimo_pedido()
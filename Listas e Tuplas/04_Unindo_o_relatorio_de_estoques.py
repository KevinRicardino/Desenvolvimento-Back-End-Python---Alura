'''
Unindo o relatório de estoques:

Armano trabalha com a gestão de dois estoques de mercadorias que 
são representados como tuplas. Agora, ele precisa criar um relatório 
unificado com os produtos dos dois estoques juntos.

Para ajudá-lo, como você criaria um programa que ler as informações 
dos estoques e gera um relatório com todos os produtos juntos?

Exemplo de Entrada:

    Produtos do estoque 1 (separados por vírgula): Arroz, Feijão, Macarrão
    Produtos do estoque 2 (separados por vírgula): Óleo, Sal, Açúcar

Saída esperada:

    Estoque combinado:
    ('Arroz', 'Feijão', 'Macarrão', 'Óleo', 'Sal', 'Açúcar')
'''

def unir_estoques():
    '''Lê os produtos de dois estoques e exibe um relatório unificado.'''

    # Entrada dos produtos dos dois estoques
    estoque1 = input('Produtos dos estoque 1 (separados por vírgula): ')
    estoque2 = input('Produtos do estoque 2 (separados por vírgula): ')

    # Converte as entradas em tuplas, removendo espaços extras
    estoque1_tuple = tuple(produto.strip() for produto in estoque1.split(','))
    estoque2_tuple = tuple(produto.strip() for produto in estoque2.split(','))

    # Une as duas tuplas
    estoque_combinado = estoque1_tuple + estoque2_tuple

    # Exibe o relatório final
    print('\nEstoque combinado:')
    print(estoque_combinado)

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    unir_estoques()
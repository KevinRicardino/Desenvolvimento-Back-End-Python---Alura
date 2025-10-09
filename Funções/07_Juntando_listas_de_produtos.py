'''
Juntando listas de produtos:

Clara está gerenciando o estoque de sua loja e recebeu duas listas 
separadas: uma contendo os nomes dos produtos e outras com seus 
respectivos preços. Para facilitar a organização, ela precisa combinar 
essas listas de forma que cada produto seja associado ao seu preço.

Crie um programa que junte as listas e exiba o resultado no formato 
produto: preço

Exemplo de entrada:

    Digite os produtos separados por vírgula: maça, banana, pera

    Digite os preços separados por vírgula: 2.5, 1.2, 3.0

Saída esperada:

    maça: 2.5
    banana: 1.2
    pera: 3.0
'''

def juntar_listas():
    '''
    Solicita listas de prrodutos e preços e exibe o resultado combinando ambos.
    '''

    # Solicita as entradas
    produtos = input('Digite os produtos separados por vírgula: ').split(',')
    precos = input('Digite os preços separados por vírgula: ').split(',')

    # Remove espaços extras e converte os preços para float
    produtos = [p.strip() for p in produtos]
    precos = [float(p.strip()) for p in precos]

    # Junta as listas com zip e exibe o resultado
    for produto, preco in zip(produtos, precos):
        print(f'{produto}: {preco}')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    juntar_listas()
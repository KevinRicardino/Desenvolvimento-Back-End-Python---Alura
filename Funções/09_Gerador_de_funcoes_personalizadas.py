'''
Gerador de funções personalizadas:

Miguel está desenvolvendo um sistema de cupons de desconto e 
precisa de uma forma para aplicar diferentes taxas de desconto 
sobre os valores das compras.

Diante deste problema, crie uma closure que gere uma função 
capaz de calcular o preço final com um desconto fixo definido 
pelo usuário.

Exemplo de entrada:

    Digite a porcentagem de desconto: 10
    Digite o valor da compra: 200

Saída esperada:

    Preço final com desconto: 180.0
'''

def aplicar_desconto():
    '''
    Solicita a porcentagem de desconto e o valor da compra,
    e exibe o preço final com desconto.
    '''

    # Solicita os dados do usuário
    desconto = float(input('Digite a porcentagem de desconto: '))
    valor_compra = float(input('Digite o valor da compra: '))

    # Cria a closure para aplicar o desconto
    calcular = lambda valor: valor * (1 - desconto / 100)

    # Calcula e exibe o preço final
    preco_final = calcular(valor_compra)
    print(f'Preço final com desconto: {preco_final}')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    aplicar_desconto()
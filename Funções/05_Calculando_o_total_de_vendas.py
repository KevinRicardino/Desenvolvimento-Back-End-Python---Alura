'''
Calculando o total de vendas:

Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. 
As vendas são informadas em uma única linha separadas por espaços.

Sua tarefa é criar um programa que receba essa linha, converta os valores para números 
e exiba o total.

Exemplo de entrada:

    Digite os valores das vendas: 100 250 300

Saída esperada:

    O total de vendas foi: 650
'''

def calcular_total_vendas():
    '''
    Solicita os valores das vendas, converte para números e exibe o total.
    '''

    # Solicita os valores de venda
    entrada = input('Digite os valores das vendas: ')

    # Converte os valores para float e soma
    vendas = [float(valor) for valor in entrada.split()]
    total = sum(vendas)

    # Exibe o resultado
    print(f'O total de vendas foi: {total:.0f}')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    calcular_total_vendas()
'''
Filtrando números pares:

Lucas está desenvolvendo um sistema para gerar relatórios 
financeiros e precisa filtrar apenas os valores pares de 
uma lista de números informada pelo usuário.

Crie um programa que receba uma lista de números e exiba 
apenas os pares usando a função filter().

Exemplo de entrada:

    Digite os números separados por espaço: 1 2 3 4 5 6 

Saída esperada:

    Números pares: 2 4 6 
'''

def filtrar_pares():
    '''
    Solicita uma lista de números e exibe apenas os pares usando filter().
    '''

    # Solicita os números
    entrada = input('Digite os números sepaarados por espaço: ')

    # Converte para inteiros
    numeros = [int(num) for num in entrada.split()]

    # Filtra apenas os pares
    pares = list(filter(lambda x: x % 2 == 0, numeros))

    # Exibe o resultado
    print('Números pares:', *pares)

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    filtrar_pares()
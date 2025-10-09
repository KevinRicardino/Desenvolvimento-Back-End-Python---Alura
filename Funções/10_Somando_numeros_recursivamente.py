'''
Somando números recursivamente:

Paulo está desenvolvendo um programa para calcular valores acumulados 
em um sistema financeiro. Ele precisa somar os todos os números inteiros 
de 1 até n, onde n é um valor escolhido pelo usuário.

Ajude Paulo criando uma função recursiva que receba um número n e retorne 
a soma de todos os números inteiros de 1 até N.

Exemplo de entrada:

    Digite um número: 5

Saída esperada:

    A soma de 1 a 5 é: 15
'''

def somar_numeros():
    '''
    Solicita um número ao usuário e exibe a soma de 1 até n usando recursão.
    '''

    # Solicita o número
    n = int(input('Digite um número: '))

    # Função recursiva dentro da principal
    def soma_recursiva(x):
        if x == 1:
            return 1
        return x + soma_recursiva(x - 1)
    
    # Calcula e exibe o resultado
    resultado = soma_recursiva(n)
    print(f'A soma de 1 a {n} é: {resultado}')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    somar_numeros()
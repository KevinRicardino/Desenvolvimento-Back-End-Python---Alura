'''
Calculadora com lambda:

Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.

Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.

Exemplo de entrada:

    Digite o primeiro número: 10
    Digite o segundo número: 5
    Escolha a operação (| + | - | * | / |): +

Saída esperada:

    O resultado é: 15
'''

def calculadora_lambda():
    '''
    Solicita dois números e um operador, e calcula o resultado usando funções lambda
    '''

    # Solicita os números e o operador
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operador = input('Escolha a operação (| + | - | * | / |): ')

    # Define as funções lambda para cada operação
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else 'Erro: divisão por zero'
    }

    # Calcula e exibe o resultado
    if operador in operacoes:
        resultado = operacoes[operador](num1, num2)
        print(f'O resultado é: {resultado}')
    else:
        print('Operador inválido.')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    calculadora_lambda()
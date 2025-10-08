'''
Calculando a idade:

Julia é professora e precisa de um programa para ajudar seus alunos a calcularem 
suas idades com base no ano de nascimento. Sua tarefa é criar uma função que receba 
o ano de nascimento e o ano atual e retorne à idade correspondente.

Exemplo de entrada:

    Digite o ano de nascimento: 2005
    Digite o ano atual: 2025

Saída esperada:
   
    A idade é 20 anos.
'''

def calcular_idade():
    '''Solicitaa o ano de nascimento e o ano atual, e calcula a idade correspondente.'''
    
    # Solicita os anos
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    ano_atual = int(input('Digite o ano atual: '))

    # Calcula a idade
    idade = ano_atual - ano_nascimento

    # Exibe o resultado
    print(f'A idade é {idade} anos.')

# Executa a funçãoo principal apenas se o arquivo for executado diretamente
if __name__ =='__main__':
    calcular_idade()
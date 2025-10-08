'''
Contador de caracteres:

Sara está participando de um concurso de escrita, e uma das regras 
exige que cada palavra de seu texto tenha um limite máximo de caracteres.

Ajude Sara criando uma função que receba uma palavra e exiba a 
quantidade de caracteres.

Exemplo de entrada:

    Digite uma palavra: tecnologia

Saída esperada:

    Essa palavra tem 10 caracteres.
'''

def contar_caracteres():
    '''Solicita uma palavra e exibe a quantidade de caracteres que ela possui.'''

    # Solicita a palavra
    palavra = input('Digite uma palavra: ')

    # Calcula o número de caracteres
    quantidade = len(palavra)

    # Exibe o resultado
    print(f'Essa palavra tem {quantidade} caracteres.')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    contar_caracteres()
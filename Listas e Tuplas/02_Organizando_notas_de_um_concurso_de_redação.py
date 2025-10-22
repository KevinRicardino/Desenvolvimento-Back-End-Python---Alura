'''
Organizando notas de um concurso de redação:

Uma escola realizou um concurso de redação, e o próximo passo é organizar as notas 
dos participantes para definir a ordem de premiação. Para garantir transparência, as 
notas precisam ser classificadas em ordem crescente, do menor para o maior valor.

Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as 
notas de todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente.

Exemplo de Entrada:

    Notas: [85, 70, 90, 60, 75]

Saída esperada:

    Notas ordenadas: [60, 70, 75, 85, 90]
'''

def organizar_notas():
    '''Recebe uma lista de notas e exibe em ordem crescente.'''

    # Solicita ao usuário as notas separadas por vírgula
    entrada = input('Digite as notas separadas por vírgula: ')

    # Converte a string em lista e números inteiros
    notas = [int(nota.strip()) for nota in entrada.split(',')]

    # Ordena a lista
    notas.sort()

    # Exibe o resultado
    print(f'Notas ordenadas: {notas}')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    organizar_notas()
'''
Encontrando números em um texto:

João é atendente em uma farmácia e precisa verificar se um cliente 
forneceu um número de receita válido em uma descrição. O número da 
receita é sempre o único número presente no texto fornecido pelo cliente. 
Ele quer um programa que extraia esse número diretamente e confirme se o 
texto está correto, sem a necessidade de trabalhar com listas ou loops.

Com base nesse cenário, crie um programa que receba um texto com uma 
descrição e exiba uma mensagem com o número encontrado.

Exemplo de Entrada:

    Digite a descrição da receita: A receita 1087568 foi enviada pelo cliente.

Saída esperada:

    O número da receita é: 1087568
'''

import re

def encontrar_numero_receita():
    '''Extrai o número da receita de um texto usandoo expressões regulares.'''

    while True:
        texto = input('Digite a descrição da receita (ou "sair" para encerrar): ').strip()

        if texto.lower() == 'sair':
            print('Encerrando busca...')
            break

        # Busca um número no texto usando regex
        numero = re.search(r'\d+', texto)

        if numero:
            print(f'O número da receita é: {numero.group()}')
        else:
            print('Nenhum número de receita encontrado no texto.')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    encontrar_numero_receita()
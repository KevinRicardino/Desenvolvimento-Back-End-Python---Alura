'''
Corrigindo posições na lista de uma corrida de atletismo:

O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista 
com a classificação final dos participantes. Mas, um erro foi identificado: 
um dos nomes está incorreto. O organizador precisa de um programa que permita 
localizar o nome errado e substituí-lo pelo correto.

Como você escreveria um programa que solicite o nome errado, o nome correto 
e atualize a lista exibindo a nova classificação ao final?

Exemplo de Entrada:

    Digite o nome incorreto: Carlos
    Digite o nome correto: João

Saída esperada: 

    O nome Carlos foi substituído por João.
    Lista atualizada: ['Ana', 'João', 'Pedro']
'''

def corrigir_classificacao():
    '''Substitui um nome incorreto na lista de classificação por um nome correto.'''

    # Lista inicial de classificação com um erro
    classificacao = ['Ana', 'Carlos', 'Pedro']
    print(f'Classificação atual: {classificacao}')

    # Solicita o nome incorreto e o correto
    nome_incorreto = input('Digite o nome incorreto: ')
    nome_correto = input('Digite o nome correto: ')

    # Verifica se o nome incorreto está na lista
    if nome_incorreto in classificacao:
        indice = classificacao.index(nome_incorreto)
        classificacao[indice] = nome_correto
        print(f'\nO nome {nome_incorreto} foi substituído por {nome_correto}.')
    else:
        print(f'\nO nome {nome_incorreto} não foi encontrado na lista.')

    # Exibe a lista atualizada
    print(f'Lista atualizada: {classificacao}')

# Executa a função principal aapenas se o arquivo for executado diretamente
if __name__ == '__main__':
    corrigir_classificacao()
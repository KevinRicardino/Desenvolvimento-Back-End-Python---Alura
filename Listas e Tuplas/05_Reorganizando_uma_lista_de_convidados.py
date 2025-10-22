'''
Reorganizando uma lista de convidados:

Camila adora receber amigos para jantares temáticos. Para o próximo encontro, 
ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa 
fazer ajustes na lista de convidados. Camila quer adicionar novos nomes e 
organizá-los em posições específicas.

Como você criaria um programa que mostre a lista inicial, permita a inserção 
de um novo nome em uma posição escolhida e exiba a lista atualizada?

Exemplo de Entrada:

    Lista atual de convidados: ['Ana', 'Pedro', 'Carlos']
    Digite o nome do novo convidado: João
    Digite a posição na qual deseja inserir o convidado: 2

Saída esperada:

    Lista atualizada de convidados: ['Ana', 'João', 'Pedro', 'Carlos']
'''

def reorganizar_convidados():
    '''Mostra a lista inicial, insere um novo convidado em posição escolhida e exibe a lista atualizada.'''

    # Lista inicial de convidados
    convidados = ['Ana', 'Pedro', 'Carlos']
    print(f'Lista atual de convidados: {convidados}')

    # Solicita o nome e a posição para inserir
    novo_convidado = input('Digite o nome do novo convidado: ')
    posicao = int(input('Digite a posição na qual deseja inserir o convidado: '))

    # Insere o novo nome na posição escolhida (ajustando índice)
    convidados.insert(posicao -1, novo_convidado)

    # Exibe a lista atualizada
    print(f'\nLista atualizada de convidados: {convidados}')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    reorganizar_convidados()
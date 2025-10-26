'''
Gerenciando inscrições de um workshop:

Laura está organizando um workshop sobre tecnologia e precisa de um 
programa que permita remover participantes que desistiram do evento. 
O sistema armazena os participantes em um dicionário, onde cada chave 
é o nome e o valor é um conjunto com os dados do participante. O 
programa deve solicitar o nome de um participante e remover esse 
nome da lista de participantes registrados, caso exista.

Exemplo de entrada:

    participantes = { 

        "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 
        "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

    } 

    Nome do participante a ser removido: Carla 

Saída esperada:

    Lista atualizada de participantes: 
    Workshop 1: {'Alice', 'Bruno', 'Diego'} 
    Workshop 2: {'Fernanda', 'Gustavo', 'Helena'} 
'''

def remover_participante():
    '''Remove um participante de todos os workshops em que ele estiver inscrito.'''

    # Dicionário com os participantes
    participantes = {
        "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"},
        "Workshop 2": {"Fernanda", "Gustavo", "Helena"}
    }

    print('Participantes atuais:')
    for workshop, inscritos in participantes.items():
        print(f'{workshop}: {inscritos}')

    # Solicita o nome do participante a ser removido
    nome = input('\nNome do participante a ser removido: ')

    # Remove o participante de todos os workshops
    encontrado = False
    for inscritos in participantes.values():
        if nome in inscritos:
            inscritos.discard(nome)
            encontrado = True

    # Exibe mensagem e lista atualizada
    if encontrado:
        print(f'\nO participante {nome} foi removido.')
    else:
        print(f'\nO participante {nome} não estava na lista.')

    print('\nLista atualizada de participantes:')
    for workshop, inscritos in participantes.items():
        print(f'{workshop}: {inscritos}')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    remover_participante()
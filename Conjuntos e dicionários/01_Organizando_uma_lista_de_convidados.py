'''
Organizando uma lista de convidados:

Ana está organizando uma festa de aniversário e precisa de uma lista 
de convidados que não tenha repetições , pois algumas pessoas foram 
convidadas mais de uma vez por engano. Ela gostaria que o programa 
solicitasse o nome dos convidados e, ao final, exibisse a lista organizada sem repetições.

Escreva um programa que receba os nomes dos convidados até que o 
usuário digite 'sair', e ao final mostre a lista de convidados 
sem repetições.

Exemplo de entrada:

    Digite o nome do convidado: Ana 
    Digite o nome do convidado: João 
    Digite o nome do convidado: Ana 
    Digite o nome do convidado: Carla 
    Digite o nome do convidado: sair 

Saída esperada:

    Convidados confirmados: Ana, João, Carla 
'''

def organizar_convidados():
    '''Organiza a lista de convidados sem repetições.'''

    convidados = set() # Usando conjunto para evitar nomes duplicados

    while True:
        nome = input('Digite o nome do convidado (ou "sair" para encerrar): ').strip().capitalize()

        if nome.lower() == 'sair':
            print('\nEncerrando o cadastro de convidados...\n')
            break

        convidados.add(nome)

    # Exibe a lista final organizada
    if convidados:
        print('Convidados confirmados:', ', '.join(sorted(convidados)))
    else:
        print('Nenhum convidado foi adicionado.')

# Executa a função princiapl apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    organizar_convidados()
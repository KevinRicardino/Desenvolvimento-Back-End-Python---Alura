'''
Analisando os participantes de uma maratona:

Lucas é voluntário na organização de uma maratona e recebeu a 
lista de participantes com suas respectivas idades. Agora, ele 
precisa de um programa que apresente três informações:

- Os nomes de todos os participantes.
- As idades de todos os participantes.
- Uma relação completa com o nome e a idade de cada um.

Sua tarefa é criar esse programa com base nas informações fornecidas.

Exemplo de entrada:

    participantes = { 

        "Mariana": 25, 

        "Carlos": 32, 

        "Beatriz": 28, 

        "Rafael": 35 

    } 

Saída esperada:

    Nomes dos participantes: Mariana, Carlos, Beatriz, Rafael 

    Idades dos participantes: 25, 32, 28, 35 

    Participantes e suas idades: 

    - Mariana: 25 anos 

    - Carlos: 32 anos 

    - Beatriz: 28 anos 

    - Rafael: 35 anos 
'''

def idade_valida(valor):
    '''
    Verifica se o valor digitado é um número inteiro positivo.
    '''
    return valor.isdigit() and int(valor) > 0

def obter_participantes():
    '''
    Solicita os nomes e idades dos participantes da maratona.
    Retorna um dicionário com o formato {nome: idade}.
    '''
    participantes = {}

    print('=== Cadastro de Participantes da Maratona ===\n')

    while True:
        nome = input('Digite o nomme do participante (ou "sair" para encerrar): ').strip()

        if not nome: # Evita entradas vazias
            print('O nome não pode estar em branco.\n')
            continue

        if nome.lower() == 'sair':
            print('\nCadastro encerrado.\n')
            break

        idade = input(f'Digite a idade de {nome}: ').strip()

        if not idade_valida(idade):
            print('Idade inválida. Digite apenas números inteiros positivos.\n')
            continue

        nome_formatado = nome.title()
        participantes[nome_formatado] = int(idade)
        print(f'Participante {nome_formatado} adicionado com sucesso!\n')

    return participantes

def exibir_informacoes(participantes):
    '''
    Exibe:
    - Todos os nomes dos participantes
    - Todas as idades
    - A relação completa (nome e idade)
    '''
    if not participantes:
        print('Nenhum participante foi cadastrado.')
        return
    
    print('=== Análise dos Participantes ===\n')

    # Ordena os participantes por nome para exibição organizada
    participantes_ordenados = dict(sorted(participantes.items()))

    # Nomes dos participantes
    nomes = ', '.join(participantes_ordenados.keys())
    print(f'Nomes dos participantes: {nomes}\n')

    # Idades dos participantes
    idades = ', '.join(str(valor) for valor in participantes_ordenados.values())
    print(f'Idades dos participantes: {idades}\n')

    # Relação completa
    print('Participantes e suas idades:\n')
    for nome, idade in participantes_ordenados.items():
        print(f'- {nome}: {idade} anos')

def main():
    '''
    Função principal: gerencia o fluxo do programa.
    '''
    participantes = obter_participantes()
    exibir_informacoes(participantes)

# Executa a função apenas se o arquivo for chamado diretamente
if __name__ == '__main__':
    main()
'''
Registrando dados de alunos:

Uma escola está organizando os dados dos alunos para criar um relatório resumido. 
Cada aluno tem seus dados registrados em uma única entrada, incluindo nome, idade 
e nota final no semestre. Esses dados devem ser exibidos separadamente para cada 
aluno no formato abaixo:

    Aluno: Nome
    Idade: Idade
    Nota: Nota

Ajude a escola a desenvolver um programa que registre as informações dos alunos, 
organize os dados e exiba um relatório detalhado com as informações separadamente.

Exemplo de Entrada:

    Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: João, 16, 8.5, Maria, 17, 9.2, Pedro, 15, 7.8

Saída esperada:

    Aluno: João
    Idade: 16
    Nota: 8.5

    Aluno: Maria
    Idade: 17
    Nota: 9.2

    Aluno: Pedro
    Idade: 15
    Nota: 7.8
'''

def registrar_dados_alunos():
    '''Registra e exibe os dados dos alunos em formato organizado.'''

    # Entrada dos dados de todos os alunos
    entrada = input('Digite os dados dos alunos no formato Nome, Idade, Nota separados por vírgula: ')

    # Divide os dados e remove espaços extras
    dados = [item.strip() for item in entrada.split(',')]

    # Percorre a lista de 3 em 3 (Nome, Idade, Nota)
    print()
    for i in range(0, len(dados), 3):
        nome = dados[i]
        idade = dados[i + 1]
        nota = dados[i + 2]

        print(f'Aluno: {nome}')
        print(f'Idade: {idade}')
        print(f'Nota: {nota}\n')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    registrar_dados_alunos()
'''
Validando nomes com Regex:

Lorena trabalha no setor de cadastros de uma empresa e precisa 
garantir que os nomes inseridos pelos clientes estejam no formato 
correto. O padrão esperado é que os nomes comecem com uma letra 
maiúscula e contenham apenas letras (sem números ou caracteres especiais). 
Para facilitar o trabalho, ela quer um programa que valide automaticamente 
os nomes fornecidos.

Ajude a Lorena criando um programa que solicite um nome ao usuário e 
verifique se ele atende às regras.

Exemplo de Entrada:

    Digite o nome do cliente para validação: maria123

Saída esperada:

    Nome inválido!
'''

import re

def validar_nome():
    '''Valida se o nome começa com letra maiúscula e contém apenas letras.'''

    while True:
        nome = input('Digite o nome do cliente para validação (ou "sair" para encerrar: )').strip()

        if nome.lower() == 'sair':
            print('Encerrando validação...')
            break

        # Expressão regular: começa com maiúscula, seguida de uma ou mais minúsculas
        # ^ → início | [A-Z] → letra maiúscula | [a-z]+ → uma ou mais minúsculas | $ → fim
        if re.fullmatch(r'[A-Z][a-z]+(?: [A-Z][a-z]+)*', nome):
            print('Nome válido!')

        else:
            print('Nome inválido! O nome deve começar com letra maiúscula e conter apenas letras.')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    validar_nome()
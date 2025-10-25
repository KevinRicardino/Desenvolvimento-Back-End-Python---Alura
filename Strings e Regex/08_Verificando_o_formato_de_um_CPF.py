'''
Verificando o formato de um CPF:

Sara trabalha no setor de atendimento de uma empresa e precisa 
verificar rapidamente se os clientes estão digitando seus números 
de CPF no formato correto antes de registrar os dados no sistema.

O formato esperado do CPF é: três blocos de 3 dígitos separados 
por pontos (.), seguidos por um bloco de 2 dígitos separados por um traço (-).

Ajude Sara a criar um programa que solicite o CPF de um cliente 
e verifica se ele está no formato correto.

Exemplo de Entrada:

    Digite o CPF no formato XXX.XXX.XXX-XX: 123.456.789-00

Saída esperada:

    O CPF está no formato correto.
'''

import re

def validar_cpf():
    '''Valida se o CPF informado está no formato XXX.XXX.XXX-XX'''

    while True:
        cpf = input('Digite o CPF no formato XXX.XXX.XXX-XX (ou "sair" para encerrar): ').strip()

        if cpf.lower() == 'sair':
            print('Encerrando validação de CPF...')
            break

        # Regex para o formato de CPF
        # ^ → início | \d{3} → 3 dígitos | \. → ponto literal | - → traço literal | $ → fim
        if re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            print('O CPF está no formato correto.')
        else:
            print('CPF inválido! O formato correto é XXX.XXX.XXX-XX.')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    validar_cpf()
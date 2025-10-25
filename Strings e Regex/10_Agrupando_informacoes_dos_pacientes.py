'''
Agrupando informações dos pacientes:

Carlos é analista de dados em um hospital e está organizando informações de 
pacientes em um banco de dados. Ele recebe os dados no formato: 
"PrimeiroNome Sobrenome - Ano". Por exemplo, “Monalisa Silva - 1994”.

Carlos precisa de um programa que leia as informações, capture cada parte 
separadamente, nome, o sobrenome e o ano de nascimento para preencher os 
campos do sistema.

Ajude Carlos criando um programa que solicite o nome completo e o ano de 
nascimento de um paciente e exiba-os separadamente.

Exemplo de Entrada:

    Digite o nome completo e o ano de nascimento do paciente: Ana Silva - 1990

Saída esperada:

    Primeiro Nome: Ana
    Sobrenome: Silva
    Ano de Nascimento: 1990
'''

import re

def agrupar_informacoes_paciente():
    '''Captura e exibe separadamente o primeiro nome, sobrenome e ano de nascimento.'''

    entrada = input('Digite o nome completo e o ano de nascimento do paciente: ')

    # Usando regex para capturar o padrão "PrimeiroNome Sobrenome - Ano"
    padrao = r'^(\w+)\s+(\w+)\s*-\s*(\d{4})$'
    resultado = re.match(padrao, entrada)

    if resultado:
        primeiro_nome = resultado.group(1)
        sobrenome = resultado.group(2)
        ano_nascimento = resultado.group(3)

        print(f'Primeiro Nome: {primeiro_nome}')
        print(f'Sobrenome: {sobrenome}')
        print(f'Ano de Nascimento: {ano_nascimento}')

    else:
        print('Formato inválido. Certifique-se de digitar no formato "Nome Sobrenome - Ano".')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == "__main__":
    agrupar_informacoes_paciente()
              
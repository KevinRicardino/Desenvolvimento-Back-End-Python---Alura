'''
Formatando uma saudação:

Rafaela trabalha na área de marketing e quer criar mensagens 
personalizadas para os clientes. Ela precisa de um programa 
que permita exibir saudações baseadas no nome do cliente e na 
cidade onde ele mora.

Crie um programa que solicite o nome e a cidade de um cliente 
e exiba uma mensagem de boas-vindas personalizada.

Exemplo de Entrada:

    Digite o nome do cliente: Laura
    Digite a cidade do cliente: Rio de Janeiro

Saída esperada:

    Olá, Laura! Bem-vinda ao sistema da cidade de Rio de Janeiro.
'''

def saudacao_personalizada():
    '''Exibe uma mensagem de boas_vindas personalizada com base no nome e cidade do cliente.'''

    while True:
        nome = input('Digite o nome do cliente (ou "sair" para encerrar): ').strip()

        if nome.lower() == 'sair':
            print('Encerrando saudações...')
            break

        cidade = input('Digite a cidade do cliente: ').strip()

        print(f'Olá, {nome}! Bem-vinda ao sistema da cidade de {cidade}.')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    saudacao_personalizada()
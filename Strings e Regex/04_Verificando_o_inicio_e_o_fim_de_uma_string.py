'''
Verificando o início e o fim de uma String:

Renan está desenvolvendo um sistema que verifica se os links de sites 
parceiros começam com https:// e terminam com .com. Esses critérios 
são obrigatórios para que o site seja aprovado no cadastro. Ajude Renan 
a criar um programa que realize essa validação de forma automática.

Como você escreveria um programa que peça ao usuário uma URL e informe 
se ela é válida ou inválida?

Exemplo de Entrada:

    Digite a URL para validação: https://monitorrenan.com

Saída esperada:

    URL válida!
'''

def validar_url():
    '''Verifica se uma URL começa com "https://" e termina com ".com".'''

    while True:
        url = input('Digite a URL para validação (ou "sair" para encerrar): ').strip()

        if url.lower() == 'sair':
            print('Encerrando validação...')
            break

        if url.startswith('https://') and url.endswith('.com'):
            print('URL válida!')
        else:
            print('URL inválida! Ela deve começar com "https://" e terminar com ".com".')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    validar_url()
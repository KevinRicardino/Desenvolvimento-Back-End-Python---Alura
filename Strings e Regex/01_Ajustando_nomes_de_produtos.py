'''
Ajustando nomes de produtos:

Victor trabalha em um sistema de e-commerce e precisa organizar os nomes 
dos produtos que estão sendo cadastrados pelos lojistas. Esses nomes geralmente 
vêm com letras misturadas entre maiúsculas e minúsculas, além de espaços 
desnecessários no início e no final.

Ajude Victor a criar um programa que receba um nome de produto e o padronize, 
deixando todas as letras minúsculas e removendo os espaços extras.

Exemplo de Entrada:

    Digite o nome do produto: ChocoLAte Branco

Saída esperada:

    chocolate branco
'''

def padronizar_nome_produto():
    '''Padroniza o nome do produto removendo espaços extras e letras maiúsculas.'''

    while True:
        produto = input('Digite o nome do produto (ou "sair" para encerrar): ')

        if produto.lower() == 'sair':
            print('Encerrando padronização...')
            break

        # Remove espaços extras e converte para minúsculas
        nome_padronizado = produto.strip().lower()

        print(f'{nome_padronizado}')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    padronizar_nome_produto()
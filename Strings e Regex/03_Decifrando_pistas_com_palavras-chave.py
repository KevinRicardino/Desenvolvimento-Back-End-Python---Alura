'''
Decifrando pistas com palavras-chave:

Imagine que você precisa criar uma funcionalidade para um jogo, 
onde os jogadores recebem dicas baseadas em partes específicas 
de uma palavra-chave. Sua missão é desenvolver um programa que 
extraia trechos importantes de qualquer palavra digitada.

Escreva um programa que solicite ao usuário uma palavra e exiba 
as três primeiras e as três últimas letras.

Exemplo de Entrada:

    Digite a palavra-chave: Misterioso

Saída esperada:

    Primeiras: Mis
    Últimas: oso
'''

def decifrar_palavra_chave():
    '''Exibe as três primeiras e as três últimas letras de uma palavra informada pelo usuário.'''

    while True:
        palavra = input('Digite a palavra-chave (ou "sair" para encerrar): ').strip()

        if palavra.lower() == 'sair':
            print('Encerrando decifração...')
            break

        # Garante que a palavra tem pelo menos 3 letras
        if len(palavra) < 3:
            print('A palavra deve ter pelo menos 3 letras!')
            continue

        primeiras = palavra[:3]
        ultimas = palavra[-3:]

        print(f'Primeiras: {primeiras}')
        print(f'Últimas: {ultimas}')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    decifrar_palavra_chave()
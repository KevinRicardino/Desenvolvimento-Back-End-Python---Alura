'''
Substituindo palavras específicas:

Nathalia é uma escritora que está revisando um texto para publicação. 
Durante o processo, ela percebeu que usou a palavra "bom" repetidamente, 
quando queria expressar algo mais forte, como "ótimo". Para economizar 
tempo, Nathalia quer substituir automaticamente todas as ocorrências da 
palavra "bom" por "ótimo" no texto.

Ajude Nathalia a criar um programa que solicite um texto, a palavra que 
será substituída e a nova palavra. O programa deve exibir o texto com as 
alterações aplicadas.

Exemplo de Entrada:

    Digite o texto a ser revisado: O dia está bom, tudo está bom.`
    Qual palavra deseja substituir? bom
    Qual a nova palavra? ótimo

Saída esperada:

    O dia está ótimo, tudo está ótimo.
'''

def substituir_palavras():
    '''Substitui todas as ocorrências de uma palavra por outra em um texto informado pelo usuário.'''

    while True:
        texto = input('Digite o texto a ser revisado (ou "sair" para encerrar): ').strip()

        if texto.lower() == 'sair':
            print('Encerrando substituições...')
            break

        palavra_antiga = input('Qual palavra deseja substituir? ').strip()
        palavra_nova = input('Qual a nova palavra? ').strip()

        # Substitui todas as ocorrências da palavra antiga pela nova
        texto_revisado = texto.replace(palavra_antiga, palavra_nova)

        print(f'\nTexto revisado:\n{texto_revisado}\n')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    substituir_palavras()
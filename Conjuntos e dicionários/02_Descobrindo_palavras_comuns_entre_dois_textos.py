'''
Descobrindo palavras comuns entre dois textos:

Clara é editora de uma revista e deseja comparar dois artigos para 
identificar quais palavras aparecem em ambos. Sua tarefa é criar um 
programa que receba dois textos e exiba o conjunto de palavras comuns 
entre eles.

Exemplo de entrada:

    Texto 1: O sol brilha forte no céu azul 

    Texto 2: O céu azul anuncia um dia de sol intenso 

Saída esperada:

    Palavras em comum: {'o', 'azul', 'sol', 'céu'} 
'''

def palavras_comuns():
    '''Encontra as palavras que aparecem em ambos os textos.'''

    texto1 = input('Digite o primeiro texto: ').lower()
    texto2 = input('Digite o segundo texto: ').lower()

    # Divide os textos em palavras e transforma em conjuntos
    conjunto1 = set(texto1.split())
    conjunto2 = set(texto2.split())

    # Encontra as palavras em comum
    comuns = conjunto1 & conjunto2 # ou conjunto1.intersection(conjunto2)

    if comuns:
        print('\nPalavras em comum:', comuns)
    else:
        print('\nNão há palavras em comum entre os textos.')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    palavras_comuns()
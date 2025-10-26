'''
Comparando listas de compra:

Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. 
Elas querem um programa que mostre:

- Quais itens apareceram nas duas listas
- Quais foram exclusivos de Laura
- Quais foram exclusivos da Ana

Escreva um programa que solicite as listas e mostre os resultados dessas comparações.

Exemplo de entrada:

    Lista de Laura: leite, pão, café, açúcar 
    Lista de Ana: pão, café, biscoito, chocolate 

Saída esperada:

    Itens em ambas as listas: pão, café 
    Itens exclusivos de Laura: leite, açúcar 
    Itens exclusivos de Ana: biscoito, chocolate
'''

def comparar_listas():
    '''Compara as listas de compras de Laura e Ana.'''

    laura = input('Digite a lista de Laura (itens separados por vírgula): ').lower()
    ana = input('Digite a lista de Ana (itens separados por vírgula): ').lower()

    # Converte as listas em conjuntos, removendo espaços extras
    conjunto_laura = {item.strip() for item in laura.split(',')}
    conjunto_ana = {item.strip() for item in ana.split(',')}

    # Calcula interseção e diferenças
    ambas = conjunto_laura & conjunto_ana
    exclusivas_laura = conjunto_laura - conjunto_ana
    exclusivas_ana = conjunto_ana - conjunto_laura

    print('\nItens em ambas as listas:', ', '.join(sorted(ambas)) if ambas else 'Nenhum')
    print('Itens exclusivos de Laura:', ', '.join(sorted(exclusivas_laura)) if exclusivas_laura else 'Nenhum')
    print('Itens exclusivos de Ana:', ', '.join(sorted(exclusivas_ana)) if exclusivas_ana else 'Nenhum')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    comparar_listas()
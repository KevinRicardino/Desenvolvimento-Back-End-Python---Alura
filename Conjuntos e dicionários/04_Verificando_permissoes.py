'''
Verificando permissões:

Marina trabalha no setor de segurança de uma empresa e precisa 
verificar se um determinado conjunto de permissões faz parte das 
permissões principais de um sistema. Sua tarefa é desenvolver um 
programa que receba duas listas de permissões e verifique se a 
segunda lista está contida na primeira.

Exemplo de entrada:

    > CASO 01: 
    Permissões principais: leitura, escrita, execução, compartilhamento 
    Permissões solicitadas: leitura, escrita 

    > CASO 02: 
    Permissões principais: leitura, escrita, execução, compartilhamento 
    Permissões solicitadas: leitura, exclusão 

Saída esperada:

    > CASO 01: 
    As permissões solicitadas fazem parte das permissões principais. 

    > CASO 02: 
    As permissões solicitadas não fazem parte das permissões principais. 
'''

def verificar_permissoes():
    '''Verifica se as permissões solicitadas estão contidas nas principais.'''

    principais = input('Digite as permissões principais (separadas por vírgula): ').lower()
    solicitadas = input('Digite as permissões solicitadas (separadas por vírgula): ').lower()

    # Converte as listas em conjuntos
    conjunto_principais = {perm.strip() for perm in principais.split(',')}
    conjunto_solicitadas = {perm.strip() for perm in solicitadas.split(',')}

    # Verifica se solicitadas é subconjunto de principais
    if conjunto_solicitadas <= conjunto_principais: # ou conjunto_solicitadas.issubset(conjunto_principais)
        print('\nAs permissões solicitadas fazem parte das permissões principais.')
    else:
        print('\nAs permissões solicitadas não fazem parte das permissões principais.')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    verificar_permissoes()
'''
Verificando itens na despensa:

Roberto está organizando sua despensa e quer verificar se determinados itens já 
estão armazenados antes de adicioná-los à lista de compras.

Ajude Roberto a criar um programa que pergunte o item desejado e verifique se 
ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, 
o programa deve informar que ele precisa ser comprado.

Exemplo de Entrada:

    Digite o item que você quer verificar: açúcar

Saída esperada:

    O item açúcar precisa ser comprado.

'''

def verificar_despensa():
    '''Verifica se o item está disponível na despensa.'''

    # Lista de itens disponíveis na despensa
    despensa = ['arroz', 'feijão', 'macarrão', 'sal', 'óleo', 'café']

    while True:
        item = input('Digite o item que você quer verificar (ou "sair") para encerrar: ').lower()

        if item == 'sair':
            print('Encerrando verificação...')
            break

        if item in despensa:
            print(f'O item {item} já está disponível na despensa.')
        else:
            print(f'O itemm {item} precisa ser comprado.')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    verificar_despensa()
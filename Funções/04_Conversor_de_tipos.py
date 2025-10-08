'''
Conversor de tipos:

Pedro está criando um sistema de cadastro de produtos para sua loja e 
percebeu que todos os números de telefone dos clientes estão armazenados 
como strings. No entanto, para facilitar buscas e validações, ele precisa 
que esses números sejam tratados como inteiros.

Dado o seguinte código com uma lista de números de telefone armazenados 
incorretamente como str, faça duas funções, uma que converte os tipos 
para inteiro e outra que verifica se a conversão foi feita corretamente 
e todos os números de telefone são inteiros:

Exemplo de entrada:

    telefones = ['11987654321', '21912345678', '31987654321', '11911223344']

Saída esperada:

    Todos os números foram convertidos corretamente!
'''

def converter_para_inteiros(telefones):
    '''
    Recebe uma lista de números de telefone em formato string e retorna uma lista com os valores convertidos para inteiro.
    '''
    return [int(numero) for numero in telefones]

def verificar_conversao(telefones):
    '''
    Verifica se todos os números da lista são inteiros.
    '''
    return all(isinstance(numero, int) for numero in telefones)

# Executa o código principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    telefones = ['11987654321', '21912345678', '31987654321', '11911223344']

    # Converte os números para inteiros
    telefones_convertidos = converter_para_inteiros(telefones)

    # Verifica a conversão
    if verificar_conversao(telefones_convertidos):
        print('Todos os números foram convertidos corretamente!')
    else:
        print('A conversão falhou. Aionda há valores que não são inteiros.')

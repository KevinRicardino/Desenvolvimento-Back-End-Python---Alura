'''
Contagem Regressiva:

Aline está implementando uma funcionalidade que exibe mensagens personalizadas 
para os clientes durante uma promoção especial da sua nova loja de livros. O sistema 
deve exibir uma mensagem de contagem regressiva personalizada para cada número 
de 10 até 1, e ao final exibir a mensagem: "Aproveite a promoção agora!".

Crie um programa que utilize um laço for para exibir as seguintes mensagens:

Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".
Saída esperada:

    Faltam apenas 10 segundos - Não perca essa oportunidade!
    A contagem continua: 9 segundos restantes.
    Faltam apenas 8 segundos - Não perca essa oportunidade!
    A contagem continua: 7 segundos restantes.
    Faltam apenas 6 segundos - Não perca essa oportunidade!
    A contagem continua: 5 segundos restantes.
    Faltam apenas 4 segundos - Não perca essa oportunidade!
    A contagem continua: 3 segundos restantes.
    Faltam apenas 2 segundos - Não perca essa oportunidade!
    A contagem continua: 1 segundos restantes.
    Aproveite a promoção agora!
'''

def contagem_regressiva():
    '''Exibe uma contagem regressiva personalizada de 10 até 1.'''

    # Percorre os números de 10 até 1
    for segundos in range(10, 0, -1):
        if segundos % 2 == 0: # Números pares
            print(f'Faltam apenas {segundos} segundos - Não perca essa oportunidade!')
        else: # Números ímpares
            print(f'A contagem continua: {segundos} segundos restantes.')

    print('Aproveite a promoção agora!')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    contagem_regressiva()
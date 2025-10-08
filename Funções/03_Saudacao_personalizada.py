'''
Saudação personalizada:

Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. 
Ela deseja criar um programa que exiba uma saudação personalizada dependendo 
da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:

    Se for antes das 12h, exibir "Bom dia";
    Entre 12h e 18h, exibir "Boa tarde";
    Após 18h, exibir "Boa noite".

Exemplo de entrada:

    Digite a hora atual (0-23): 15

Saída esperada:

    Boa tarde!
'''

def saudacao_personalizada():
    '''Solicita a hora atual e exibe uma saudação personalizada com base no horário.'''

    # Solicita a hora atual
    hora = int(input('Digite a hora atual (0-23): '))

    # Verifica e exibe a saudação correspondente
    if hora < 12:
        print('Bom dia!')
    elif hora < 18:
        print('Boa tarde!')
    else:
        print('Boa noite!')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    saudacao_personalizada()

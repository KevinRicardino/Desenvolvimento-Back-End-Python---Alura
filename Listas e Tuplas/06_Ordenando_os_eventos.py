'''
Ordenando os eventos:

A Futuro Eventos, uma empresa especializada em organização de conferências, cometeu 
um erro ao registrar a sequência dos eventos de uma conferência importante. Os eventos 
foram registrados na ordem inversa à que deveriam acontecer. Agora, a equipe precisa 
corrigir a ordem dos eventos para garantir que a conferência aconteça conforme o 
planejamento original.

Considerando a lista inicial de eventos, crie um programa que permita ao organizador 
ordená-los, de forma que a lista final siga a sequência correta.

    eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']

Saída esperada:

    Ordem corrigida: ['Abertura', 'Palestra 2', 'Palestra 3', 'Encerramento']
'''

def corrigir_ordem_eventos():
    '''Inverte a ordem da lista de eventos para restaurar a sequência correta.'''

    # Lista inicial de eventos registrados incorretamente
    eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']

    print(f'Eventos registrados (ordem incorreta): {eventos_registrados}')

    # Corrige a ordem usando o método reverse() ou slicing
    eventos_registrados.reverse()

    # Exibe a lista corrigida
    print(f'Ordem corrigida: {eventos_registrados}')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    corrigir_ordem_eventos()
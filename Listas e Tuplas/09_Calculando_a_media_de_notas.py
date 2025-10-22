'''
Calculando a média de notas:

A professora Helena quer facilitar sua rotina na hora de calcular a média das 
notas finais da turma. Ela sempre anota as notas dos alunos ao longo do semestre 
e, no final, precisa de um relatório para saber se a turma está indo bem.

Para isso, ajude a professora a criar um programa que receba as notas finais de 
todos os alunos e calcule a média da turma.

Exemplo de Entrada:

    Digite as notas dos alunos separadas por vírgula: 8.5, 7.0, 9.2, 6.8

Saída esperada:

    Média final da turma: 7.88
'''

def calcular_media():
    '''Calcula a média final da turma com base nas notas digitadas pelo usuário.'''

    # Solicita as notas separadas por vírgula
    entrada = input('Digite as notas dos alunos separadas por vírgula: ')

    # Converte a entrada em lista de números float
    notas = [float(nota.strip()) for nota in entrada.split(',')]

    # Calcula a média
    media = sum(notas) / len(notas)

    # Exibe o resultado com duas casas decimais
    print(f'\nMédia final da turma: {media:.2f}')

# Executa a função principal apenas se o arquivo for executaado diretamente
if __name__ == '__main__':
    calcular_media()
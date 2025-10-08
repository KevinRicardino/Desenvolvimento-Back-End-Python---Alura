'''
Classificando estudantes por média:

Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se 
foram aprovados, ficaram de recuperação ou reprovados. As regras são:

Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado
Escreva um programa que receba três notas como entrada e calcule a média final. 

Com base na média, exiba a situação do aluno.

Saída esperada:

   Digite a primeira nota: 5.3
   Digite a segunda nota: 6.7
   Digite a terceira nota: 8.3
   Média: 6.77
   Recuperação
'''

def classificar_estudante():
    ''' Solicita três notas, calcula a média e informa aa situação do aluno.'''

# Solicita as três notas do aluno
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

# Calcula a média final
media = (nota1 + nota2 + nota3) / 3

# Exibe a média formada com duas casas decimais
print(f'Média: {media:.2f}') # Se você alterar o número, será a quantidade de casas decimais que irá aparecer

# Classifica o aluno de acordo com a média
if media >= 7:
   print('Aprovado')
elif media>= 5:
   print('Recuperação')
else:
   print('Reprovado')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
   classificar_estudante()
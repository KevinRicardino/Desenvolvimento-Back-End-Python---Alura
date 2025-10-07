'''
Calculando o tempo total de projeto:

Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: 
A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os 
valores inseridos são inválidos e não calcular o total.
Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. 
Se algum valor for negativo, mostre uma mensagem informando o erro.

Saída esperada:

   Informe os dias para a atividade A: 5
   Informe os dias para a atividade B: -8
   Informe os dias para a atividade C: 10
   Erro: Os dias não podem ser negativos.
'''

def calcular_tempo_projeto():
   ''' Solicita os dias das atividades A, B e C e calcula o total se todos forem válidos.'''

   # Solicita ao usuário os dias de cada atividade:
   atividade_a = int(input('Informe os dias para a atividade A: '))
   atividade_b = int(input('Informe os dias para a atividade B: '))
   atividade_c = int(input('Informe os dias para a atividade C: '))

   # Verifica se algum valor é negativo
   if atividade_a < 0 or atividade_b < 0 or atividade_c < 0:
      print('Erro: Os dias não podem ser negativos.')
   else:
      # Calcula o total apenas se todos os valores forem válidos
      total = atividade_a + atividade_b + atividade_c
      print(f'Tempo total do projeto: {total} dias.')

# Executa a função principal
if __name__ == '__main__':
   calcular_tempo_projeto()
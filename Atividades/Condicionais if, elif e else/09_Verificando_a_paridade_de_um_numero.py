'''
Verificando a paridade de umm número:

Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique se um número é par ou ímpar. 
Essa verificação será usada para definir ações diferentes dentro do jogo. Escreva um programa que receba um 
número inteiro e exiba uma mensagem informando se ele é par ou ímpar.

Saída esperada:

   Digite um número inteiro: 20
   O número é par.
'''

def verificar_paridade():
   ''' Solicita um número inteiro e informa se ele é par ou ímpar.'''

# Solicita o número inteiro ao usuário
numero = int(input('Digite um número inteiro: '))

# Verifica a paridade do número
if numero % 2 == 0:
   print('O número é par.')
else:
   print('O número é ímpar.')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
   verificar_paridade()
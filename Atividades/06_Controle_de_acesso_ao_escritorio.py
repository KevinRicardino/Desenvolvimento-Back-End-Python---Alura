'''
Controle de acesso ao escritório:

Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar. 
Para isso, ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. Crie um programa que receba a hora atual como 
entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado.

Saída esperada:

   Digite a hora atual (formato 24 horas): 21
   Acesso negado.
'''

def verificar_acesso():
   ''' Solicita a hora atual e informa se o acesso ao escritório é permitido.'''

# Solicita a hora atual ao usuário
hora = int(input('Digite a hora atual (formato 24 horas): '))

# Verifica se o horário está dentro do período permitido
if 8 <= hora < 18:
   print('Acesso permitido.')
else:
   print('Acesso negado.')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
   verificar_acesso()
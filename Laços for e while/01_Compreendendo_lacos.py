'''
Compreendendo laços:
Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar relatórios mensais. 
Para isso, ela precisa escrever um programa que percorra a lista de nomes e exiba cada cliente.

   clientes = ['João', 'Maria', 'Carlos', 'Ana', 'Beatriz']

Ajude Ana a decidir entre usar um laço for ou while. Escreva o programa usando o laço que você acredita 
ser mais adequado para essa tarefa e explique por que escolheu esse laço.
'''

def listar_clientes():
   ''' Percorre uma lista de clientes e exibe cada um.'''

   clientes = ['João', 'Maria', 'Carlos', 'Ana', 'Beatriz']

   # Uso do laço for: ideal para percorrer listas de tamanho conhecido
   for cliente in clientes:
      print(f'Cliente: {cliente}')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
   listar_clientes()
'''
O que é um loop infinito?

André está testando um novo recurso no backend do Buscante que processa dados em um loop. 
Durante os testes, ele percebeu que o sistema parou de responder, 
e suspeita que o problema está em um loop infinito.

   contador = 0

   while contador < 10:
      print('Processando dados...')

Qual é o problema do código de André e como resolver?
'''

def processar_dados():
   ''' Exibe uma mensagem enquanto processa os dados, sem criar loop infinito.'''

   contador = 0

   # O problema do código original: o contador nunca é incrementado, criando um loop infinito.
   while contador < 10:
      print('Processando dados...')
      contador += 1 # É uma forma abreviada de escrever (contador = contador + 1).

# Executa a função principal apenas se o arquivo for executado diretamente.
if __name__ == '__main__':
   processar_dados()
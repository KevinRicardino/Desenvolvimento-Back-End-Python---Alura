'''
Quantas vezes a mensagem será exibida?

Marcos está desenvolvendo um programa para exibir uma mensagem de boas-vindas 
repetidamente no console, como parte de uma campanha de marketing de sua plataforma 
chamada Buscante. Ele quer garantir que a mensagem seja exibida 5 vezes.

Ajude Marcos a escrever um programa que exiba a mensagem: "Bem-vindo ao Buscante!" 
o número exato de vezes que ele precisa.

Saída esperada:

   Bem-vindo ao Buscante!
   Bem-vindo ao Buscante!
   Bem-vindo ao Buscante!
   Bem-vindo ao Buscante!
   Bem-vindo ao Buscante!
'''

def exibir_mensagem():
   ''' Exibe a mensagem de boas-vindas 5 vezes.'''

   for i in range(5):
      print('Bem-vindo ao Buscante!')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
   exibir_mensagem()
''' 
Monitoramento de Vendas no Comércio:

Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. 
Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. 
Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.
Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. 
Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

Saída esperada:

   Digite a quantidade de maças vendidas: 15
   Digite a quantidade de bananas vendidas: 3
   As maças tiveram mais vendas.

'''

# Solicita ao usuário a quantidade de maças vendidas
macas = int(input('Digite a quantidade de maças vendidas: '))

# Solicita ao usuário a quantidade de bananas vendidas
bananas = int(input('Digite a quantidade de bananas vendidas: '))

# Compara as vendas e decide qual produto teve mais vendas
if macas > bananas:
   print('As maças tiveram mais vendas.')
elif bananas > macas:
   print('As bananas tiveram mais vendas.')
else: 
   print('Houve empate nas vendas.') # Caso as quantidades sejam iguais
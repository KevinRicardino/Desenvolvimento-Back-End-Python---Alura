'''
Calculando a soma de números:

Você está recebendo uma lista de valores representando os produtos de sua loja virtual e 
gostaria de calcular a soma total desses produtos para entender o desempenho financeiro semanal.

   valores = [10, 20, 30, 40, 50]

Crie um programa para implementar a soma.

Saída esperada:

   A soma total das receitas é: 150
'''

def calcular_soma():
   '''Calcula a soma total dos valores de produtos.'''

   valores = [10, 20, 30, 40, 50]
   soma = 0 # variável acumuladora
   
   # Percorre cada valor na lista e acumula a soma
   for valor in valores:
       soma += valor

   print(f'A soma total das receitas é: {soma}')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    calcular_soma()

'''
Calculando pedágio:

Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. 
O valor do pedágio depende da distância percorrida:

Até 100 km: R$ 10,00
Entre 100 km e 200 km: R$ 20,00
Acima de 200 km: R$ 30,00
Crie um programa que receba a distância percorrida e informe o valor do 
pedágio correspondente.

Saída esperada:

   Digite a distância percorrida (em km): 250
   Valor do pedágio: R$ 30,00
'''

def calcular_pedagio():
   ''' Solicita a distância percorrida e exibe o valor do pedágio correspondente.'''

# Solicita a distância ao usuário
distancia = float(input('Digite a distância percorrida (em km): '))

# Determina o valor do pedágio de acordo com a distância
if distancia <= 100:
   valor = 10.00
elif distancia <= 200:
   valor = 20.00
else:
   valor = 30.00

# Exibe o valor do pedágio formatado
print(f'Valor do pedágio: R$ {valor:.2f}') # Se você alterar o número, será a quantidade de casas decimais que irá aparecer

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
   calcular_pedagio()
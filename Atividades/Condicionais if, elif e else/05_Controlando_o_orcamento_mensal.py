'''
Controlando o orçamento mensal:

Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. 
Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. 
O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

Saída esperada:

   Digite o total de despesas do mês (R$): 5897.58
   Atenção! Você ultrapassou o limite do orçamento.
'''

def controlar_orcamento():
   ''' Solicita o total de despesas e informa se o limite de orçamento foi ultrapassado.'''

# Define o limite de orçaamento
limite = 3000.00

# Solicita o total de despesas do usuário
despesas = float(input('Digite o total de despesas do mês (R$): '))

# Verifique se o usuário ultrapassou o limite de orçamento
if despesas > limite:
   print('Atenção! Você ultrapassou o limite do orçamento.')
else:
   print('Parabéns! Você está dentro do limite do orçamento.')

# Executa a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
   controlar_orcamento()
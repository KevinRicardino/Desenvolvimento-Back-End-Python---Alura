'''
Temperatura dos Servidores:

Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. 
Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

Saída esperada:

   Digite a temperatura atual: 30
   Alerta! Temperatura acima do limite permitido.
'''

def verificar_temperatura():
   ''' Recebe a temperatura atual e exibe um alerta se estiver acima do limite.'''

   # Solicita ao usuário a temperatura atual (em graus Celsius)
   temperatura = float(input('Digite a temperatura atual: '))

   # Define o limite máximo permitido
   LIMITE = 25.0

   # Verifica se a temperatura ultrapassa o limite
   if temperatura > LIMITE:
      print('Alerta! Temperatura acima do limite permitido.')
   else:
      print('Temperatura dentro do limite seguro.')

# Executta a função principal apenas se o arquivo for executado diretamente
if __name__ == '__main__':
   verificar_temperatura()
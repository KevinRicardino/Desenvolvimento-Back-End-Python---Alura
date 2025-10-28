'''
Criando classes, construtores e métodos:

Na classe ContaBancaria, adicione um método especial __str__ que 
retorna uma mensagem formatada com o titular e o saldo da conta. 
Crie duas instâncias da classe e imprima essas instâncias.
'''

class ContaBancaria:
    def __init__(self, titular = '', saldo = int, ativo = False):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular: {self._titular} - Saldo: {self._saldo}'
    
conta1 = ContaBancaria('Maia', 1000)
conta2 = ContaBancaria('Kamala', 2000)

print(conta1)
print(conta2)
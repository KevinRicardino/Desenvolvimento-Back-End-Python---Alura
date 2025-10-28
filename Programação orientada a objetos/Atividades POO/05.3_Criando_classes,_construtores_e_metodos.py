'''
Criando classes, construtores e métodos:

Adicione um método de classe chamado ativar_conta à classe 
ContaBancaria que define o atributo ativo como True. Crie 
uma instância da classe, chame o método de classe e imprima 
o valor de ativo.
'''

class ContaBancaria:
    def __init__(self, titular = '', saldo = int, ativo = False):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular: {self._titular} - Saldo: {self._saldo}'
    
    @classmethod
    def ativar_conta(self):
        self._ativo = True
        print(f'Status da conta {self._ativo}')
    
conta1 = ContaBancaria('Maia', 1000)
conta2 = ContaBancaria('Kamala', 2000)

print(conta1)
conta1.ativar_conta()
print(conta2)
conta2.ativar_conta()
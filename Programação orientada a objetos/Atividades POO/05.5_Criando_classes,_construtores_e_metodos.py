'''
Criando classes, construtores e métodos:

Crie uma instância da classe e imprima o valor 
da propriedade titular.
'''

class ContaBancaria:
    def __init__(self, titular = '', saldo = int, ativo = False):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False

    @property
    def titual(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._titular
    
    @property
    def ativo(self):
        return self._ativo
    
conta1 = ContaBancaria('Maia', 1000)
conta2 = ContaBancaria('Kamala', 2000)
conta3 = ContaBancaria('Alana', 5000)

print(f'Titular da conta 1 {conta1._titular}')
print(f'Titular da conta 2 {conta2._titular}')
print(f'Titular da conta 3 {conta3._titular}')
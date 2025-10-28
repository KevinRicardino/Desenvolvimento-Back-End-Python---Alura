'''
Criando classes, construtores e métodos:

Refatore a classe ContaBancaria para utilizar a abordagem 
"pythonica" na criação de atributos. Utilize propriedades, 
se necessário.
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
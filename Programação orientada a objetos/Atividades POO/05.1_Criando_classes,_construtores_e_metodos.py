'''
Criando classes, construtores e métodos:

Crie uma classe chamada ContaBancaria com um construtor que aceita os 
parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
'''

class ContaBancaria:
    def __init__(self, titular = '', saldo = int, ativo = False):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False
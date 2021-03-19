# !/usr/bin/python3
# encoding: iso-8859-1
"""
Esta funcao visa realizar operações matematicas, somar, subtrair e multiplicar
"""
import random


class Geranumeros(object):
    """ Classe para gerar numeros inteiros em um range de 0 a numero
    ;numero: Numero final do range do randint"""

    def __init__(self, numero: int) -> None:
        self.__numero: int = random.randint(0, numero)

    @property
    def numero(self) -> int:
        """Getter do atributo numero"""
        return self.__numero


class Operacoes(object):
    """Classe para definir as operações e para isso é preciso dois numeros inteiros
    ;primeiro_numero: Numero inteiro para realizar uma das operações
    ;segundo_numero: Numero inteiro para realizar uma das operações"""

    def __init__(self, primeiro_numero: int, segundo_numero: int):
        self.__primeiro_numero = primeiro_numero
        self.__segundo_numero = segundo_numero

    @property
    def primeiro_numero(self) -> int:
        """ Getter do primeiro numero da soma"""
        return self.__primeiro_numero

    @property
    def segundo_numero(self) -> int:
        """Getter do segundo numero da soma"""
        return self.__segundo_numero


class Somar(Operacoes):
    """ Classe para realizar soma de dois numeros"""

    def __init__(self, primeiro_numero, segundo_numero):
        super(Somar, self).__init__(primeiro_numero, segundo_numero)

    def mensagem(self):
        """Imprime a conta que precisa ser feita para o usuario"""
        print(f'Qual o resultado da soma?\n{self.primeiro_numero} + {self.segundo_numero} = ?')

    def somar(self) -> int:
        """Retorna soma de dois numeros"""
        return self.primeiro_numero + self.segundo_numero


class Subtrair(Operacoes):
    """ Classe para realizar subtração de dois numeros"""

    def __init__(self, primeiro_numero, segundo_numero):
        super(Subtrair, self).__init__(primeiro_numero, segundo_numero)

    def mensagem(self):
        """Imprime a conta que precisa ser feita para o usuario"""
        if self.primeiro_numero >= self.segundo_numero:
            print(f'Qual o resultado da subtrção?\n{self.primeiro_numero} - {self.segundo_numero} ?')
        elif self.primeiro_numero < self.segundo_numero:
            print(f'Qual o resultado da subtrção?\n{self.segundo_numero} - {self.primeiro_numero} ?')

    def subtrair(self) -> int:
        """Retorna a subtracao de dois numeros"""
        if self.primeiro_numero >= self.segundo_numero:
            return self.primeiro_numero - self.segundo_numero
        elif self.primeiro_numero < self.segundo_numero:
            return self.segundo_numero - self.primeiro_numero


class Multiplicar(Operacoes):
    """Classe para realizar a muiltiplicação de dois numeros"""

    def __init__(self, primeiro_numero, segundo_numero):
        super(Multiplicar, self).__init__(primeiro_numero, segundo_numero)

    def mensagem(self):
        """Imprime a conta que precisa ser feita para o usuario"""
        print(f'Qual o resultado da multiplicação?\n{self.primeiro_numero} * {self.segundo_numero} = ?')

    def multiplicar(self) -> int:
        """Retorna multiplicação de dois numeros"""
        return self.primeiro_numero * self.segundo_numero


class EscolheOperacoes(Operacoes):
    """Classe para escolher qual das 3 operações será realizada"""

    def __init__(self, primeiro_numero, segundo_numero):
        super(EscolheOperacoes, self).__init__(primeiro_numero, segundo_numero)

    def escolhe_operacoes(self) -> int:
        """Imprime a conta a ser feita pelo usuario e retorna o resultado para o programa"""
        operacao = random.choice(['Somar', 'Subtrair', 'Multiplicar'])
        if operacao == 'Somar':
            Somar(self.primeiro_numero, self.segundo_numero).mensagem()
            return Somar(self.primeiro_numero, self.segundo_numero).somar()
        elif operacao == 'Subtrair':
            Subtrair(self.primeiro_numero, self.segundo_numero).mensagem()
            return Subtrair(self.primeiro_numero, self.segundo_numero).subtrair()
        elif operacao == 'Multiplicar':
            Multiplicar(self.primeiro_numero, self.segundo_numero).mensagem()
            return Multiplicar(self.primeiro_numero, self.segundo_numero).multiplicar()

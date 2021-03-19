# !/usr/bin/python3
# encoding: iso-8859-1
"""
Seleciona uma dificuldade atraves do nivel de range final passado, com base no atributo nivel
"""


from operacoes import EscolheOperacoes, Geranumeros


class Dificuldade(object):
    """Realiza o processo de escolher uma das dificuldade encaminhando os parametros para a escolha da operação."""

    def __init__(self, nivel: int):
        self.__nivel = nivel

    @property
    def nivel(self) -> int:
        """Getter do nivel escolhido"""
        return self.__nivel

    def dificuldade(self) -> int:
        """Com base na escolha da dificuldade do usuario, passa os parametros para gerar a operação"""
        if self.nivel == 1:
            return EscolheOperacoes(Geranumeros(20).numero, Geranumeros(20).numero).escolhe_operacoes()
        elif self.nivel == 2:
            return EscolheOperacoes(Geranumeros(40).numero, Geranumeros(40).numero).escolhe_operacoes()
        elif self.nivel == 3:
            return EscolheOperacoes(Geranumeros(60).numero, Geranumeros(60).numero).escolhe_operacoes()
        elif self.nivel == 4:
            return EscolheOperacoes(Geranumeros(999).numero, Geranumeros(999).numero).escolhe_operacoes()
        elif self.nivel == 5:
            return EscolheOperacoes(Geranumeros(9999).numero, Geranumeros(9999).numero).escolhe_operacoes()
        else:
            return EscolheOperacoes(Geranumeros(9999 * self.nivel).numero, Geranumeros(9999 * self.nivel).numero).\
                escolhe_operacoes()

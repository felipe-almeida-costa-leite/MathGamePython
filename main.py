# !/usr/bin/python3
# encoding: iso-8859-1
"""
Este programa visa fundamentar os conhecimentos do curso, atrav�s de um jogo.
Enunciado:

1 - Devemos desenvolver uma aplica��o onde ao ser inicializada solicite ao usu�rio escolher o n�vel de
dificuldade do jogo

2 - Ap�s isso gera e apresenta, de forma aleta�ria, um c�lculo para que possamos informar o resultado.

3 - Iremos limitar as opera��es em somar, diminuir e multiplicar. Se o usu�rio acertar a resposta, somar� 1 ponto ao seu
score. Acertando ou errando, ele poder� ou n�o continuar o jogo

"""
from jogar import Jogar

if __name__ == '__main__':
    nome: str = str(input('Digite o nome do Participante: '))
    Jogar(nome).jogar()

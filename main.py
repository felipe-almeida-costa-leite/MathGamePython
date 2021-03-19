# !/usr/bin/python3
# encoding: iso-8859-1
"""
Este programa visa fundamentar os conhecimentos do curso, através de um jogo.
Enunciado:

1 - Devemos desenvolver uma aplicação onde ao ser inicializada solicite ao usuário escolher o nível de
dificuldade do jogo

2 - Após isso gera e apresenta, de forma aletaória, um cálculo para que possamos informar o resultado.

3 - Iremos limitar as operações em somar, diminuir e multiplicar. Se o usuário acertar a resposta, somará 1 ponto ao seu
score. Acertando ou errando, ele poderá ou não continuar o jogo

"""
from jogar import Jogar

if __name__ == '__main__':
    nome: str = str(input('Digite o nome do Participante: '))
    Jogar(nome).jogar()

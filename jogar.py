# !/usr/bin/python3
# encoding: iso-8859-1
"""
Funcao e tarefas para jogar o game MathGamePython
"""
from seleciona_dificuldade import Dificuldade


class Jogar(object):
    """ Classe para jogar o jogo MathGamePython - Basic"""

    def __init__(self, nome: str):
        self.__nome = nome

    @property
    def nome(self):
        """Getter do atributo nome"""
        return self.__nome

    def jogar(self):
        """Jogar o Game MathGamePython"""
        pontoinicial = 0
        vidas = 5
        continuar = ''
        print(f'Bem vindo {self.nome} ao jogo MathGamePython')
        while True:
            if continuar != 'Sair':
                dificuldade: int = int(input('Selecione a dificuldade ou digite Sair para encerrar o jogo: '))
                if dificuldade == 'Sair':
                    break
                else:
                    while True:
                        conta: int = int(Dificuldade(dificuldade).dificuldade())
                        resultado: int = int(input('Digite o resultado da conta:  '))
                        if conta == resultado:
                            pontoinicial += 100 ** dificuldade
                            print(f'Parabens {self.nome}, você acertou!\nVocê ainda tem {vidas} vidas e fez '
                                  f'{pontoinicial}')
                        else:
                            continuar = str(
                                input(f'OPS! Você errou!\nVocê ainda tem {vidas} vidas, e fez {pontoinicial} pontos\n'
                                      f'Digite Enter para continuar\nDigite Sair para encerrar o jogo ou Alterar para '
                                      f'alterar a dificuldade: '))
                            if continuar == 'Sair':
                                print(
                                    f'Parabens {self.nome}, você jogou muito bem Obrigado por jogar MathGamePython\n'
                                    f'Este Game foi produzido por Felipe A C Leite\nMe siga no linkedin\nObrigado')
                                break
                            elif continuar == '':
                                continue
                            elif continuar == 'Alterar':
                                break
                    if continuar == 'Sair':
                        break
                    elif continuar == 'Alterar':
                        continue
            else:
                break

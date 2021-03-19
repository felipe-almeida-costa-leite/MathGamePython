# !/usr/bin/python3
# encoding: iso-8859-1
import random


def operacoes(range, dificuldade):
    conta = 0
    primeiro_numero = random.randint(0, range)
    segundo_numero = random.randint(0, range)
    operacao = random.choice(['+', '-', '*'])
    print(primeiro_numero)
    print(segundo_numero)
    print(operacao)
    if operacao == '+':
        conta = f'{primeiro_numero} {operacao} {segundo_numero} = ?'
        print(conta)
        resultado = int(input('Digite o resultado: '))
        conta = primeiro_numero + segundo_numero
        if conta == resultado:
            print('Parabens, você acertou!')
            return 100 * (dificuldade ** 2)
        else:
            print('Você errou')
            return 0
    elif operacao == '-':
        if primeiro_numero > segundo_numero:
            conta = f'{primeiro_numero} {operacao} {segundo_numero} = ?'
            print(conta)
            conta = primeiro_numero - segundo_numero
        elif primeiro_numero < segundo_numero:
            conta = f'{segundo_numero} {operacao} {primeiro_numero} = ?'
            print(conta)
            conta = segundo_numero - primeiro_numero
        elif primeiro_numero == segundo_numero:
            conta = 0
        resultado = int(input('Digite o resultado: '))
        if conta == resultado:
            print('Parabens, você acertou!')
            return 100 * (dificuldade ** 2)
        else:
            print('Você errou')
            return 0
    elif operacao == '*':
        conta = f'{primeiro_numero} {operacao} {segundo_numero} = ?'
        print(conta)
        resultado = int(input('Digite o resultado: '))
        conta = primeiro_numero * segundo_numero
        if conta == resultado:
            print('Parabens, você acertou!')
            return 100 * (dificuldade ** 2)
        else:
            print('Você errou')
            return 0


def seleciona_dificuldade() -> int:
    dificuldade = int(input('Selecione a dificuldade: '))
    if dificuldade == 1:
        return operacoes(20, dificuldade)
    elif dificuldade == 2:
        return operacoes(40, dificuldade)
    elif dificuldade == 3:
        return operacoes(60, dificuldade)
    elif dificuldade == 4:
        return operacoes(999, dificuldade)


def jogar() -> None:
    pontoinicial = 0
    print('Bem vindo ao jogo')
    while True:
        ponto = seleciona_dificuldade()
        if ponto >= 100:
            pontoinicial += ponto
            jogar_ou_nao = input(f'Sua pontuação é {pontoinicial}\nDigite enter para continuar jogando ou Sair pra encerrar o jogo: ')
            if jogar_ou_nao == 'Sair':
                break
            else:
                continue

jogar()

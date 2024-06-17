# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!
import random
from os import system, name
import csv

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

print("\n******************* Calculadora em Python *******************")

def operação():
    global operador
    escolha = 0
    while 1 > escolha or 4 < escolha:
        escolha = int(input('---------\nEscolha a operação, digitando o respectivo número\n[1] - Soma\n[2] - Substração\n[3] - Multiplicação\n[4] - Divisão\n---------\n'))
        if 1 <= escolha <= 4:
            break
    if escolha == 1:
        operador = 1
        return 
    elif escolha == 2:
        operador = 2
        return
    elif escolha == 3:
        operador = 3
        return
    elif escolha == 4:
        operador = 4
        return

def resultado():
    operação()
    num = float
    if operador == 1:
        num = round(m + n,8)
        print(f'---------\n{m} + {n} = {num}\nO resultado é igual a {num}')
    elif operador == 2:
        num = round(m - n,8)
        print(f'---------\n{m} - {n} = {num}\nO resultado é igual a {num}')
    elif operador == 3:
        num = round(m * n,8)
        print(f'---------\n{m} x {n} = {num}\nO resultado é igual a {num}')
    elif operador == 4:
        num = round(m / n,8)
        print(f'---------\n{m} / {n} = {num}\nO resultado é igual a {num}')
    resposta = int(input('---------\nVocê deseja realizar outra operação?\n[1] - Sim\n[2] - Não\n---------\n'))
    while resposta == 1:
        a = float(input('---------\nInsira o segundo número:\n'))
        operação()
        if operador == 1:
            num_n = round(num + a,8)
            print(f'---------\n{num} + {a} = {num_n}\nO resultado é igual a {num_n}')
            num = num_n
            resposta = int(input('---------\nVocê deseja realizar outra operação?\n[1] - Sim\n[2] - Não\n---------\n'))
        elif operador == 2:
            num_n = round(num - a,8)
            print(f'---------\n{num} - {a} = {num_n}\nO resultado é igual a {num_n}')
            num = num_n
            resposta = int(input('---------\nVocê deseja realizar outra operação?\n[1] - Sim\n[2] - Não\n---------\n'))
        elif operador == 3:
            num_n = round(num * a,8)
            print(f'---------\n{num} x {a} = {num_n}\nO resultado é igual a {num_n}')
            num = num_n
            resposta = int(input('---------\nVocê deseja realizar outra operação?\n[1] - Sim\n[2] - Não\n---------\n'))
        elif operador == 4:
            num_n = round(num / a,8)
            print(f'---------\n{num} / {a} = {num_n}\nO resultado é igual a {num_n}')
            num = num_n
            resposta = int(input('---------\nVocê deseja realizar outra operação?\n[1] - Sim\n[2] - Não\n---------\n'))
    print(f'---------\nO resultado é igual a {num}\n-----------Fim da operação-----------')
    return

if __name__ == "__main__":
    limpa_tela()
    m = float(input('\nInsira o primeiro número:\n'))
    n = float(input('\nInsira o segundo número:\n'))
    resultado()
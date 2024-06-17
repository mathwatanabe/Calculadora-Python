# Esse projeto consiste em uma calculadora Python simples, com operações de adição, subtração, multiplicação e divisão, sem ter uma preocupação com o desempenho e simplificação do código. O objetivo desse projeto é apenas
# desenvolver alguns conhecimentos referentes à linguagem Python na prática.

# A linha de código abaixo é necessária para ter acesso ao módulo OS, que possui ferramentas para interagir com o Sistema Operacional.
from os import system, name

# Esse bloco de código é uma função necessária para realizar uma limpeza de tela sempre que o programa é executado para assim ter uma tela com as informações da execução atual.
def limpa_tela():
    # Esse condicional serve para acessar um sistema operacional específico e executar a limpeza de tela. Essa cláusula if realiza uma busca se o Sistema Operacional é o Windows. O comando para essa limpeza de tela no
    # Windows é 'cls'.
    if name == 'nt':
        _ = system('cls')
    # Para outros Sistemas Operacionais, como Linux e MacOS, é necessária a execução de outro comando ('clear')
    else:
        _ = system('clear')
        
# O primeiro passo escolhido para o desenvolvimento do código foi uma função capaz de realizar uma das quatro operações básicas.
def operação():
    # Foi necessário definir a variável operador como global para utilizá-la posteriormente na função "resultado()", que realiza o cálculo desejado. Se não ocorresse esta definição, o programa apresentaria uma mensagem de
    # erro, pois a variável não estaria definida.
    global operador
    # A sequência de bloco de código com um loop while foi colocada para evitar que o usuário do programa escolha alguma operação diferente das quatro operações definidas.
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
    print("\n****************** Calculadora em Python ******************")
    m = float(input('\nInsira o primeiro número:\n'))
    n = float(input('\nInsira o segundo número:\n'))
    resultado()

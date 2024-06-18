<h1><b>Calculadora Python</b></h1>

## Objetivo
O presente projeto tem por objetivo apresentar o desenvolvimento de uma calculadora programada com a linguagem Python para realizar as quatro operações básicas (soma, subtração, multiplicação e divisão) entre dois números determinados pelo usuário. Não estava no planejamento do trabalho realizar um trabalho pensando na simplificação e otimização do tempo de execução do código, mas sim o aprimoramento e desenvolvimento de conceitos e fundamentos vistos na prática.

## Ferramentas
* Python 3.9.13

## Desenvolvimento
Os principais mecanismos da calculadora foram as duas funções criadas dentro do código. Uma chamada de <code>operação()</code> para pedir e guardar a escolha de operação do usuário em uma variável chamada de <code>operador</code>. Tal variável foi definida como global para ser utilizada na função seguinte.
```neon
def operação():
    global operador
    escolha = 0
    while 1 > escolha or 4 < escolha:
        escolha = int(input('---------\nEscolha a operação, digitando o respectivo número\n[1] - Soma\n[2] - Substração\n[3] - Multiplicação\n[4] - Divisão\n---------\n'))
        if 1 <= escolha <= 4:
            break
```
O resto do código da função operação() se encontra nos arquivos hospedados como '<a href="https://github.com/mathwatanabe/Calculadora-Python/blob/main/calculadora_v1.py">calculadora_v1.py</a>' e com maiores explicações em '<a href="https://github.com/mathwatanabe/Calculadora-Python/blob/main/Calculadora_v1_notebook.ipynb">Calculadora_v1_notebook.ipynb</a>'.

Outra função chamada de <code>resultado()</code> é utilizada com o valor guardado na variável <code>operador</code> para realizar a operação desejada, seguindo uma das claúsulas condicionais da função <code>resultado()</code> a partir da escolha do usuário. Parte do código é apresentado abaixo:
```neon
def resultado():
    operação()
    num = float
    if operador == 1:
        num = round(m + n,8)
        print(f'---------\n{m} + {n} = {num}\nO resultado é igual a {num}')
```
Dentro dessa função ainda há um loop exigindo que o usuário determine se deseja realizar outra operação ou não.
```neon
def resultado():
    ...

    while 1 > resposta or 2 < resposta:
        resposta = int(input('---------\nVocê deseja realizar outra operação?\n[1] - Sim\n[2] - Não\n---------\n'))
```
A função pode seguir para dois caminhos, o de execução de uma nova operação e o de finalização. Uma nova operação segue o padrão abaixo:
```neon
def resultado():
    ...

    while resposta == 1:
        a = float(input('---------\nInsira o segundo número:\n'))
        operação()
        resposta = 0
        if operador == 1:
            num_n = round(num + a,8)
            print(f'---------\n{num} + {a} = {num_n}\nO resultado é igual a {num_n}')
            num = num_n
            while 1 > resposta or 2 < resposta:
                resposta = int(input('---------\nVocê deseja realizar outra operação?\n[1] - Sim\n[2] - Não\n---------\n'))
```
Já para a finalização, a função finaliza com a utilização do termo <code>return</code>, finalizando assim o código.
```neon
def resultado():
    ...

    print(f'---------\nO resultado é igual a {num}\n-----------Fim da operação-----------')
    return
```
Os blocos são executados conforme demonstrado abaixo:
```neon
if __name__ == "__main__":
    limpa_tela()
    print("\n******************* Calculadora em Python *******************")
    m = float(input('\nInsira o primeiro número:\n'))
    n = float(input('\nInsira o segundo número:\n'))
    resultado()
```

import math

def som(a, b):
    return a + b

def pro(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

while True:
    print(25*'<>')
    print('Calculadora')
    print(25*'<>')
    print('Opção:')
    print('1-SOMA')
    print('2-SUBTRAÇÃO')
    print('3-MULTIPLICAÇÃO')
    print('4-DIVISÃO')
    print('5-COSSENO')
    print('6-SENO')
    print('7-TANGENTE')
    print('8-SAÍDA')
    print(25*'<>')
    op = int(input('Qual a opção? '))
    if op in [1, 2, 3, 4]:
        num1 = float(input('Insira o primeiro número? '))
        num2 = float(input('Insira o segundo número? '))
        if op == 1:
            result = som(num1, num2)
        elif op == 3:
            result = pro(num1, num2)
        elif op == 2:
            result = sub(num1, num2)
        elif op == 4:
            result = div(num1, num2)
        print('{:.2f}'.format(result))
    elif op in [5, 6, 7]:
        num1 = int(input('Insira o número? '))
        if op == 5:
            result = math.acos(num1)
        elif op == 6:
            result = math.asin(num1)
        elif op == 7:
            result = math.atan(num1)
        print('{:.2f}'.format(result))
    elif op == 8:
        break

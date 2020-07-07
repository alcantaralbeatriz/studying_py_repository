#67 Faça um programa que leia um número inteiro e forneça a tabuada, utilizando WHILE.

def Main067():
    a = b = 0
    while True:
        a = int(input('Quer ver a tabuada de que valor? '))
        if a <= 0:
            break
        for b in range (0,11):
            print(f'{a} x {b} = {a*b:.0f}')
            b += 1

Main067()
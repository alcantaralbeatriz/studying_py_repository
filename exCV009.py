#9 Faça um programa que leia um número inteiro e forneça a tabuada.

def Main009():
    num = int(input('Digite um número inteiro: '))
    print('-'*12)
    for x in range(0,11):
        print(f'{num} x {x:2} = {x*num}')
    print('-'*12)

Main009()

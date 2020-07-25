#38. Faça um programa que leia dois números e diga qual o maior e o menor deles, ou se são iguais.

def Main038():
    num_1 = int(input('Digite o primeiro número: '))
    num_2 = int(input('Digite o segundo número: '))
    if num_1 == num_2:
        print(f'{num_1} e {num_2} são iguais.')
    elif num_1 > num_2:
        print(f'{num_1} é maior que {num_2}.')
    elif num_1 < num_2:
        print(f'{num_2} é maior que {num_1}.')

Main038()


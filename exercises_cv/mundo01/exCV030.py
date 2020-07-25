#30. Faça um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

def Main030():
    numero_usuario = int(input('Digite um número qualquer: '))
    teste = numero_usuario % 2
    if teste == 0:
        print(f'O número {numero_usuario} é par!')
    else:
        print(f'O número {numero_usuario} é ímpar!')

Main030()
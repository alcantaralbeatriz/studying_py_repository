#23. Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

def Main023():
    numero = int(input('Número de 0 a 9999: '))
    print(f'Unidade: {(numero // 1) % 10}\n'
        f'Dezena: {(numero // 10) % 10}\n'
        f'Centena: {(numero // 100) % 10}\n'
        f'Milhar: {(numero // 1000) % 10}')

Main023()

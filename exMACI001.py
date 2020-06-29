# Faça um programa que dada uma sequencia de numeros inteiros, terminada por zero, imprima seus quadrados e raiz quadrada.
import math

def Main():
    num = 1
    while num != 0:
        num = int(input('Digite seu número inteiro: '))
        print(f'O quadrado de {num} é {num**2:.1f} e sua raiz quadrada é {math.sqrt(num):.2f}')
    print('End!')

Main()
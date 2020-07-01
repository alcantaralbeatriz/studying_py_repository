#6 Faça um programa que leia um número e mostre seu dobro, triplo e raiz quadrada.

import math

def Main006():
    num = int(input('Digite um número inteiro: '))
    print(f'O dobro é {2*num}, o triplo é {3*num}, e a raiz quadrada é {math.sqrt(num):.2f}')

Main006()
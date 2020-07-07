#18. Faça um programa que leia um ângulo qualquer e mostre o valor de seno, cosseno, e tangente.

import math

def Main018():
    angulo = float(input('Qual o ângulo: '))
    print(f'O seno é {math.sin(math.radians(angulo)):.2f}')
    print(f'O cosseno é {math.cos(math.radians(angulo)):.2f}')
    print(f'A tangente é {math.tan(math.radians(angulo)):.1f}')


Main018()
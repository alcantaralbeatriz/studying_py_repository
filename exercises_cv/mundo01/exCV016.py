#16. Escreva um programa que leia um numero real qualquer e mostre apenas a sua porção inteira. (Truncar)

import math

def Main016():
    real_qualquer = float(input('Digite um número qualquer: '))
    print(f'A parte inteira é {math.trunc(real_qualquer)}')

# OU {real_qualquer:.0f} 
# OU .format(int(real_qualquer))
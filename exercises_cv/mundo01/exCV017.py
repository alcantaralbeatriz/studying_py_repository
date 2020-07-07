#17. Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre a hipotenusa.

import math
def Main017():
    cateto_oposto = int(input('Cateto oposto: '))
    cateto_adjacente = int(input('Cateto adjacente: '))
    
    print(f'A hipotenusa é: {math.hypot(cateto_oposto,cateto_adjacente):.2f}')

#print(f'A hipotenusa é: {math.sqrt(cateto_oposto**2+cateto_adjacente**2)}'
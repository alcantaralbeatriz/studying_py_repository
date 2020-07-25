#35. Faça um programa que leia o comprimento de 3 retas e retorne ao usuário se elas podem ou não formar um triângulo.

def Main035():
    reta_a = int(input('Reta A: '))
    reta_b = int(input('Reta B: '))
    reta_c = int(input('Reta C: '))
    if reta_a < reta_b + reta_c and reta_b < reta_a + reta_c and reta_c < reta_b + reta_a:
        print('Formará um triângulo!')
    else:
        print('NÃO formará um triangulo')

Main035()
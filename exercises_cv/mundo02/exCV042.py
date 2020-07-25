#42. Faça um programa que leia o comprimento de 3 retas e retorne ao usuário se elas podem ou não formar um triângulo, e se é equilátero, isósceles ou escaleno.

def Main042():
    reta_a = int(input('Reta A: '))
    reta_b = int(input('Reta B: '))
    reta_c = int(input('Reta C: '))
    if reta_a < reta_b + reta_c and reta_b < reta_a + reta_c and reta_c < reta_b + reta_a:
        if reta_a == reta_b and reta_b == reta_c and reta_a == reta_c:
            print('Formará um triângulo equilátero!')
        elif reta_a == reta_b or reta_b == reta_c or reta_a == reta_c:
            print('Formará um triângulo isósceles!')
        elif reta_a != reta_b and reta_b != reta_c and reta_a != reta_c:
            print('Formará um triângulo escaleno!')
    else:
        print('NÃO formará um triangulo')

Main042()
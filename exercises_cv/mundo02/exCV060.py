#60. Faça um programa que leia um número inteiro e mostre seu fatorial. 

def Main060():
    num_inteiro = int(input('Digite um número inteiro: '))
    print(f'{num_inteiro}! = ', end='')
    fatorial = 1
    for x in range(num_inteiro,0,-1):
        fatorial *= x
        if x == 1:
            print(f'{x} = ', end='')
        else:
            print(f'{x} * ', end='')
    print(fatorial)

Main060()
#52. Faça um programa que leia um número inteiro e mostre se ele é primo ou não, mostrando seus divisíveis.

def Main052():
    num_inteiro = int(input('Digite o número: '))
    cont = 0
    for x in range(1,num_inteiro + 1):
        if num_inteiro % x == 0:
            print('\033[1;32m', end='')
            cont += 1
        print(f'{x}\033[m ', end='')
    print(f'\n\033[mO número {num_inteiro} é divisível por {cont} números e ', end='')
    if cont == 2 or cont == 1:
        print('é \033[4mprimo\033[m!')
    elif cont > 2:
        print('\033[4mnão\033[m é primo!')

Main052()
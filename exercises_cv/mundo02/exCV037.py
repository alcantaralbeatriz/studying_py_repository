#37. Faça um programa que leia um número inteiro qualquer e peça ao usuário escolher qual será a base de conversão: 1 - Binário, 2 - Octal, e 3 - Hexadecimal.

def Main037():
    num_inteiro = int(input('Digite um número inteiro na base decimal: '))
    print('Agora escolha a base de conversão.\n'
    '1 - Binário\n'
    '2 - Octal\n'
    '3 - Hexadecimal\n')
    base = int(input('Qual a base de conversão desejada? '))
    if base == 1:
        print(f'O número {num_inteiro} equivale a {bin(num_inteiro)[2:]}.')
    elif base == 2:
        print(f'O número {num_inteiro} equivale a {oct(num_inteiro)[2:]}.')
    elif base == 3:
        print(f'O número {a} equivale a {hex(num_inteiro).upper()[2:]}.')
    else:
        print('Escolha inválida!')

Main037()

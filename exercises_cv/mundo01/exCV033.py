#33. Faça um programa que leia três números e diga qual o maior e o menor deles. Utilizando if e else.

def Main033():
    print('Me dê 3 números!')
    a = float(input('Primeiro número: '))
    b = float(input('Segundo número: '))
    c = float(input('Terceiro número: '))
    if a > b:
        if b > c:
            print(f'Ordem crescente: {a} > {b} > {c}')
        else:
            print(f'Ordem crescente: {c} > {a} > {b}') if c > a else print(f'Ordem crescente: {a} > {c} > {b}')
    else:
        if a>c:
            print(f'Ordem crescente: {b} > {a} > {c}')
        else:
            print(f'Ordem crescente: {c} > {b} > {a}') if c > b else print(f'Ordem crescente: {b} > {c} > {a}')

Main033()
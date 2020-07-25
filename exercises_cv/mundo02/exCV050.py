#50. Faça um programa que receba 6 números inteiros e some os pares.

def Main050():
    soma = contagem = 0
    print('Me dê 6 numeros inteiros!')
    for x in range(1,7):
        num = int(input(f'Digite o {x}º valor: '))
        if 0 == num % 2:
            soma += num; contagem += 1
    print(f'A soma dos {contagem} números PARES é {soma}!')

Main050()
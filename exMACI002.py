# Faça um programa que some os primeiros n números positivos de uma sequência (1 a infinito).

def Main():
    n = int(input('Digite o n a ser somado: '))
    somapos = 0
    for sub in range(0,n+1):
        somapos = somapos + sub
    print(f'A soma dos{n} primeiros números positivos é {somapos}.')

Main()
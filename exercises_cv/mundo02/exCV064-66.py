#64. Faça um programa que leia vários números inteiros, e use '999' como condição de parada. Ao final, mostre quantos números foram digitados e qual foi a soma entre eles.

#66. Faça um programa que leia vários números inteiros, e use '999' como condição de parada. Ao final, mostre quantos números foram digitados e qual foi a soma entre eles. Utilize o 'break'. (junto do exercício 64)

def Main064():
    num_inteiro = int(input('Digite um número inteiro, exceto 999(parada): '))
    qtdd_num = somatoria = 0
    while num_inteiro != 999:
        somatoria += num_inteiro
        qtdd_num += 1
        num_inteiro = int(input('Digite um número, exceto 999(parada): '))
    print(f'Números digitados: {qtdd_num}; Soma dos números: {somatoria}')

def Main066():
    num_inteiro = qtdd_num = somatoria = 0
    while True:
        num_inteiro = int(input('Digite um número inteiro, exceto 999(parada): '))
        if num_inteiro == 999:
            break
        somatoria += num_inteiro
        qtdd_num += 1
    print(f'Números digitados: {qtdd_num}; Soma dos números: {somatoria}')


Main066()
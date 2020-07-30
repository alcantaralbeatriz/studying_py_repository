#51. Faça um programa que leia o primeiro termo e a razão de uma PA (progressão aritmética), e mostre os 10 primeiros termos.

def Main051():
    primeiro_termo = int(input('Digite o primeiro termo da PA: '))
    razao = int(input('Digite a razão da PA: '))
    prox_num = primeiro_termo + (10 * razao)
    print('Os 10 primeiros termos da sua PA são: ')
    for x in range(primeiro_termo, prox_num, razao):
        print(x, end='.. ')

Main051()
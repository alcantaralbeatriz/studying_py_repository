#61. Faça um programa que leia o primeiro termo e a razão de uma PA (progressão aritmética), e mostre os 10 primeiros termos; utilizando estrutura while. (51 melhorado)

def Main061():
    primeiro_termo = int(input('Digite o primeiro termo da PA: '))
    termo = primeiro_termo
    razao = int(input('Digite a razão da PA: '))
    cont = 0
    qtdd_termos = 10
    print('Dez primeiros termos da sua PA:', end='')
    while cont < qtdd_termos:
        if cont == (qtdd_termos - 1):
            print(f'{termo}.')
        else:
            print(f'{termo}.. ', end='')
        termo += razao
        cont += 1

Main061()



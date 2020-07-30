#62. Faça um programa que leia o primeiro termo, a razão de uma PA (progressão aritmética), e quantos termos o usuário quer ver; utilizando estrutura while, e encerrando se o usuário escolher "0" termos a mais.

def PA(termo, razao, qtdd):
    cont = 0
    print('Termos da sua PA: ', end='')
    while cont < qtdd:
        if cont == (qtdd - 1):
            print(f'{termo}.')
        else:
            print(f'{termo}, ', end='')
        termo += razao
        cont += 1

def Main062():
    n = True
    while n == True:
        qtdd_termos = int(input('Quantos termos deseja visualizar: '))
        if qtdd_termos == 0:
            print('Obrigado, fim.')
            n = False
        else:
            primeiro_termo = int(input('Digite o primeiro termo da PA: '))
            razao = int(input('Digite a razão da PA: '))
            PA(primeiro_termo, razao, qtdd_termos)

Main062()

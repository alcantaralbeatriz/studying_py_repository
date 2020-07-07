#82 Faça um programa que o usuário forneca valores numericos em uma lista. Serão exibidos todos os valores, e outras duas listas com numeros pares e impares.

def Main082():
    numeros = list()
    pares = list()
    impares = list()
    resposta = 's'
    while resposta in ['S','s']:
        valor = int(input('Digite o valor a ser adicionado: '))
        numeros.append(valor)
        if valor % 2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)
        resposta = input('Deseja continuar? [S/N] ').upper()
        if resposta in ['n','N']:
            break

    print(f'Sua lista ficou: {sorted(numeros)}\n'
            f'Os pares: {sorted(pares)}\n'
            f'Os impares: {sorted(impares)}.')

Main082()
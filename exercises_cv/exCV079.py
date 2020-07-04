#79 Faça um programa que o usuário forneca vários valores numericos, e cadastre-os em uma lista. Caso o número já exista, ele não será adicionado. No fim, serão exibidos todos os valores únicos digitados, em ordem crescente.

def Main079():
    numeros = list()
    resposta = 's'
    while resposta in ['S','s']:
        valor = int(input('Digite o valor a ser adicionado: '))
        if valor in numeros:
            print('Esse valor já existe, não será adicionado.')
        else:
            print('Valor adicionado com sucesso!')
            numeros.append(valor)
        resposta = input('Deseja continuar? [S/N] ').upper()
        if resposta in ['n','N']:
            break
    
    print(f'Sua lista ficou: {sorted(numeros)}')


Main079()
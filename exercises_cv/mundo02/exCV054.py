#54. Faça um programa que leia o ano de nascimento de sete pessoas, e mostre quantas atingiram e quantas não atingiram a maioridade.

import datetime

def Main054():
    print('Digite os anos dos nascimentos da..')
    contagem_maiores = contagem_menores = 0
    ano_atual = datetime.date.today().year
    for x in range(1, 8):
        ano_nascimento = int(input(f'{x}ª pessoa: '))
        idade = ano_atual - ano_nascimento
        if idade >= 18:
            contagem_maiores += 1 
        else:
            contagem_menores += 1
    print(f'Ao todo, {contagem_maiores} pessoas são maiores de idade!')
    print(f'Ao todo, {contagem_menores} pessoas são menores de idade!')

Main054()
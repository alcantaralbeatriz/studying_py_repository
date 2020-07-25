#41. Faça um programa que leia o ano de nascimento de um atleta e mostre sua categoria.

import datetime

def Main041():
    ano_nascimento = int(input('Diga meu jovem, qual o ano de seu nascimento?'))
    ano_atual = int(datetime.date.today().year)
    idade = ano_atual - ano_nascimento
    print('Você pertence à ',end='')
    if idade <= 9:
        print('categoria Mirim')
    elif idade > 9 and idade <= 14:
        print('categoria Infantil')
    elif idade > 14 and idade <= 19:
        print('categoria Júnior')
    elif idade <= 20 and idade > 19:
        print('categoria Sênior')
    elif idade > 20:
        print('categoria Master')

Main041()

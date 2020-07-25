#32. Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import datetime

def Main032():
    hoje = int(input('Que ano gostaria de saber se é bissexto?'))
    #OU hoje = datetime.date.today().year
    if hoje % 4 == 0 and hoje % 100 != 0 or hoje % 400 == 0:
        print(f'O ano {hoje} é Bissexto!')
    else:
        print(f'O ano {hoje} NÃO é Bissexto!')

Main032()
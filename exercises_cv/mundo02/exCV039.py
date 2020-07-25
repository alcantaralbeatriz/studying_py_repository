#39. Faça um programa que leia o ano de nascimento de um jovem e informe se ele ainda irá se alistar, se é a hora de se alistar ou se já passou o tempo, além de mostrar o tempo que falta ou que passou para o alistamento.

import datetime

def Main039():
    ano_nascimento = int(input('Diga meu jovem, qual o ano de seu nascimento?'))
    ano_atual = int(datetime.date.today().year)
    if (ano_atual - ano_nascimento) == 18:
        print('Está na hora de se alistar!')
    elif (ano_atual - ano_nascimento)>18:
        print(f'Já passou {ano_atual - ano_nascimento-18} ano(s) do prazo de se alistar!')
    elif (ano_atual - ano_nascimento)<18:
        print(f'Faltam {18-(ano_atual - ano_nascimento)} ano(s) para você se alistar!')

Main039()
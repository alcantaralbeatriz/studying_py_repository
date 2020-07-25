#46. Faça um programa que mostre uma contagem regressiva 10 a 0 para o Ano Novo.

import time

def Main046():
    print('Está chegando a hora!')
    for x in range(10,0,-1):
        print(x)
        time.sleep(1)
    print('Feliz ANO NOVO!!!')

Main046()
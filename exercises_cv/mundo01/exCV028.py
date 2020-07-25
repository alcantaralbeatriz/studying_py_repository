#28. Faça um programa que faça o computador fornecer um numero inteiro entre 0 e 5 e peça para o usuário descobrir qual numero é e diga se acertou ou não.

import random
def Main028():
    numero_aleatorio = random.randint(0,6)  #OU random.randrange(6)
    print('Estou pensando em um número, qual é?')
    numero_chute = int(input('Adivinhe qual é o número de 0 a 5:'))
    contador = 0
    if numero_aleatorio == numero_chute:
        print('Acertou!')
    else numero_aleatorio != numero_chute:
        while numero_aleatorio != numero_chute:
            print('Errou! Tente novamente!')
            numero_chute = int(input('Adivinhe de novo 0 a 5:'))
            contador += 1
    print(f'Acertou, depois de {contador} tentativas erradas.. É {numero_aleatorio}!')

Main028()
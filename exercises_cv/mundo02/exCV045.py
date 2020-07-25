#45. Faça um programa que jogue jokenpô com o usuário.

import random

def Main045():
    print('Vamos jogar JOKENPO! Qual sua opção?')
    escolha_usuario = int(input('[1] Pedra, [2] Papel, ou [3] Tesoura? '))
    x = '[1] Pedra'
    y = '[2] Papel'
    z = '[3] Tesoura'
    escolha_maquina = random.randint(1,3)
    if escolha_usuario == escolha_maquina:
        print('Empate!')
        if escolha_usuario == 1:
            print(f'VOCÊ {x} x PC {x}')
        elif escolha_usuario == 2:
            print(f'VOCÊ {y} x PC {y}')
        elif escolha_usuario == 3:
            print(f'VOCÊ {z} x PC {z}')
    elif escolha_usuario == 1:
        if escolha_maquina == 2:
            print(f'VOCÊ {x} x {y} PC\nPC ganhou!')
        elif escolha_maquina == 3:
            print(f'VOCÊ {x} x {z} PC\nVOCÊ ganhou!')
    elif escolha_usuario == 2:
        if escolha_maquinab == 1:
            print(f'VOCÊ {y} x {x} PC\nVOCÊ ganhou!')
        elif escolha_maquina == 3:
            print(f'VOCÊ {y} x {z} PC\nPC ganhou!')
    elif escolha_usuario == 3:
        if escolha_maquina == 1:
            print(f'VOCÊ {z} x {x} PC\nPC ganhou!')
        elif escolha_maquina == 2:
            print(f'VOCÊ {z} x {y} PC\nVOCÊ ganhou!')
    else:
        print(f'Opção inválida! Mas o PC jogou {escolha_maquina}...')

Main045()
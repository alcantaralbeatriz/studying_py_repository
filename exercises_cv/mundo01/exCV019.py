#19. Faça um programa que escolha um dos 4 alunos para o professor.

import random

def Main019():
    alunos = []
    for x in range(4):
        alunos.append(input(f'Nome do aluno {x}: '))
    print(f'Quem vai apagar o quadro é o/a: {random.choice(alunos)}!!')

Main019()
#20. Faça um programa que sorteie a ordem dos n alunos para o professor. (Mudei para que o professor definisse o numero de alunos a serem sorteados)

import random

def Main020():
    alunos = []
    num = int(input("Quantos alunos serão sorteados? "))
    for x in range(1,num+1):
        alunos.append(input(f'Nome do {x}º aluno: '))
    random.shuffle(alunos)
    print(f'Ordem de apresentação será:{alunos}')
    
Main020()
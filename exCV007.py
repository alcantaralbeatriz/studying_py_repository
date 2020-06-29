#7 Faça um programa que calcule a média de duas notas do aluno.

def Main007():
    nota1 = float(input('Nota da p1: '))
    nota2 = float(input('Nota da p2: '))
    media = float((nota1 + nota2) / 2)
    print(f'A média de {nota1} e {nota2} é de {media:.2f}.')

Main007()

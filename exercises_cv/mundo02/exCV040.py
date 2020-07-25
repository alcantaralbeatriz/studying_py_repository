#040 Faça um programa que calcule a média de duas notas do aluno, com resultado se foi aprovado ou não.

def Main040():
    nota_p1 = float(input('Digite a nota da P1: '))
    nota_p2 = float(input('Digite a nota da P2: '))
    media = (nota_p1 + nota_p2) / 2
    if media > 7:
        print(f'Parabéns, com a média {media:.1f}, você está Aprovado!')
    elif media >= 5 and media <= 6.9:
        print(f'Com a média {media:.1f}, você está de Recuperação!')
    elif media < 5:
        print(f'Com a média {media:.1f}, você está Reprovado!')

Main040()
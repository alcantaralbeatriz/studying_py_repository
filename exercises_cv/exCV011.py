#11 Faça um programa que leia comprimento e largura de uma parede e forneça os litros de tinta necessário para pintá-la (1.5l/m2).

def Main011():
    comprimento = float(input('Comprimento (em metros): '))
    altura = float(input('Altura (em metros): '))
    area = comprimento*altura
    print(f'A parede tem {area:.2f}m2, e precisará de {1.5*area:.1f}litros de tinta.')

Main011()

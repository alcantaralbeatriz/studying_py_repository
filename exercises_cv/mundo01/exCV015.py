#15. Escreva um programa que pergunte a quilometragem percorrida por um carro e a quantidade de dias pelo qual ele foi alugado. Calcule o preço a pagar (R$ 60,00/dia e R$ 0,15/km rodado)

def Main015():
    km_rodada = float(input('Quantos km serão rodados? '))
    dias_usados = float(input('Por quantos dias? '))
    print('Considerando 0,60 por dia e 0,15 por km rodado.'
        f'Você pagará {(dias_usados*0.6)+(km_rodada*0.15):.2f} reais.')

Main015()
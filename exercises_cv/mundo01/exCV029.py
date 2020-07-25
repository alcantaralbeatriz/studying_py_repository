#29. Faça um programa que leia a velocidade de um carro e mostre uma mensagem se ele ultrapassar 80km/h, e o valor da multa (R$ 7,00 por cada km acima do limite).

def Main029():
    velocidade_usuario = int(input('Qual a velocidade do carro (em km/h)?'))
    
    if velocidade_usuario > 80:
        print('Ultrapassou o limite!')
        valor_multa = (velocidade_usuario - 80) * 7
        print(f'A multa será de R$ {valor_multa} reais!')
    else:
        print('Está dentro do limite de velocidade!')

Main029()

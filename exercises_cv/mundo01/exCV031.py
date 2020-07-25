#31. Faça um programa que leia a distância em km de uma viagem, e calcule o valor da passagem, sendo esta de R$0,50 por km em viagens de até 200km, e R$0,45 para viagens mais longas.

def Main031():
    distancia_percorrida = float(input('Qual a distancia a ser percorrida (em km)? '))
    preco = distancia_percorrida * 0.5 if distancia_percorrida <= 200 else distancia_percorrida * 0.45
    print(f'O preço da sua passagem será de R${preco:.2f}.')

Main031()
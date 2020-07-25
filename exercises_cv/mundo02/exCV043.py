#43. Faça um programa que leia o peso e altura de uma pessoa, forneça o valor do IMC e mostre seus status.

def Main043():
    print('Vamos calcular seu IMC e categoria!')
    altura = float(input('Qual sua altura em metros: '))
    peso = float(input('Qual seu peso atual em kg: '))
    imc = peso / (altura * altura)
    print(f'Seu IMC é {imc:.1f}.', end='')
    if imc <= 18.5:
        print('Você está na categoria Abaixo do peso!')
    elif imc > 18.5 and imc <= 25:
        print('Você está na categoria Peso ideal!')
    elif imc  >25 and imc <= 30:
        print('Você está na categoria Sobrepeso!')
    elif imc > 30 and imc <= 40:
        print('Você está na categoria Obesidade!')
    elif imc > 40:
        print('Você está na categoria Obesidade Mórbida!') 

Main043()
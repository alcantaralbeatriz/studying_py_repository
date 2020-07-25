#36. Faça um programa que leia o valor de uma casa, o salario do comprador e em quantos anos ele pretende pagar, e diga se ele pode ou não obter um empréstimo (a prestação mensal não pode exceder 30% do salário).

def Main036():
    valor_casa = int(input('Qual o valor da Casa? R$: '))
    salario = int(input('Qual o valor do seu salário? R$: '))
    tempo_anos = int(input('Em quantos anos quer pagar? '))
    prestacao = valor_casa / (tempo_anos * 12)
    if prestacao > (0.3 * salario):
        print(f'Desculpe, mas o valor será de R${prestacao:.2f} por mês. Então, não poderá realizar o empréstimo.')
    else:
        print(f'Parabéns! Com a parcela de R${prestacao:.2f} por mês, você poderá fazer o empréstimo!')

Main036()
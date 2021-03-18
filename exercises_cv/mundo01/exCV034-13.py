#13. Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário após um ajuste de 15% de aumento.

def Main013():
    salario = float(input('Qual o seu salário? R$:'))
    print(f'Com o aumento de 15% fica: {salario * 1.15} reais.')

#34. Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário após um ajuste (15% para salários iguais ou até R$ 1250,00 e 15% para maiores), utilizando IF / ELSE. (ex 13 melhorado)

def Main34():
    salario = float(input('Qual o seu salário (em reais)? R$:'))
    if salario > 1250:
        print(f'Seu novo salário é de R$ {salario * 1.1:.2f}')
    else:
        print(f'Seu novo salário é de R$ {salario * 1.15:.2f}')
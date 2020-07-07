#13 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário após um ajuste de 15% de aumento.

def Main013():
    a=float(input('Qual o seu salário? R$:'))
    print(f'Com o aumento de 15% fica: {a*1.15} reais.')

#34 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário após um ajuste de 15% de aumento, utilizando IF / ELSE.

def Main34():
    b = float(input('Qual o seu salário (somente reais)? R$:'))
    if b > 1250:
        print(f'Seu novo salário é de R$ {b*1.1:.2f}')
    else:
        print(f'Seu novo salário é de R$ {b*1.15:.2f}')
#57. Faça um programa que leia o sexo de uma pessoa e só aceite "M" ou "F", caso não receba, forneça uma mensagem de erro até a resposta estiver correta.

def Main057():
    sexo = str(input("Qual o seu sexo? [M] Masculino ou [F] Feminino? ")).strip().upper()[0]
    while sexo not in 'MmFf':
        print('Erro! Digite M ou F.')
        sexo = str(input('Digite novamente: ')).upper().strip()[0]
    if sexo == 'F':
        print('Bem-vinda!')
    elif sexo == 'M':
        print('Bem-vindo!')

Main057()
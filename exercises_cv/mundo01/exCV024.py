#24. Faça um programa que leia o noem de uma cidade e diga se ela começa ou não com o nome "Santo".

#25. Faça um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

def Main024():
    nomeCidade = str(input('Cidade: ')).strip()   
    if nomeCidade[:5].upper() == 'SANTO':
        print('O nome da cidade começa com Santo.')
    else: 
        print('O nome da cidade NÃO começa com Santo.')


def Main025():
    nomeCidadao = str(input('Nome: ')).strip()
    if 'silva' in nomeCidadao.lower():
        print('Você tem Silva no sangue.')
    else:
        print('Você não tem Silva no sangue.')

Main024()
Main025()
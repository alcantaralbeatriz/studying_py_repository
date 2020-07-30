#55. Faça um programa que leia o peso de 5 pessoas e diga qual foi o menor e o maior.

def Main055():
    print('Quais os pesos?')
    for x in range(1, 6):
        if x == 1:
            peso_n = float(input(f'Digite o {x}º peso em kg: '))
            maior_peso = peso_n; menor_peso = peso_n
        else:
            peso_n = float(input(f'Digite o {x}º peso em kg: '))
            if peso_n > maior_peso:
                maior_peso = peso_n
            if peso_n < menor_peso:
                menor_peso = peso_n
    print(f'O maior valor é {maior_peso:.1f}kg.')
    print(f'O menor valor é {menor_peso:.1f}kg.')

Main055()
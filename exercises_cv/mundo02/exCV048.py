#48. Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três no intervalo de 1 a 500.

def Main048():
    soma = num_divisiveis = qtdd_numeros = 0
    print('Somando número ímpares e divisíveis por 3..')

    for x in range(1, 501, 2):
        qtdd_numeros += 1
        if x % 3 == 0:
            num_divisiveis += 1; soma += x
    print (f'Dos {qtdd_numeros} números ímpares, {num_divisiveis} são divisíveis por 3, e somados dão {soma}.\n')

Main048()
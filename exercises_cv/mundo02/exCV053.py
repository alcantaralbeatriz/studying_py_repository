#53. Faça um programa que leia uma frase e diga se é um palíndromo, desconsiderando espaços.

def Main053():
    frase = str(input('Digite a frase: '))
    frase_modificada = frase.upper().replace(' ','')
    print(f'Frase: {frase_modificada}')
    inverso = ''
    for x in range(len(frase_modificada)-1, -1, -1):
            inverso = inverso + frase_modificada[x]
    print('Inverso:', inverso)
    print('\nPalíndromo!') if inverso == frase_modificada else print('\nNão é palindromo!')

Main053()
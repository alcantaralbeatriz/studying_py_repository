#22. Faça um programa que leia o nome completo de uma pessoa e mostre: nome com todas as letras minusculas e maiusculas; quantas letras tem sem considerar espaços; e quantas letras tem o primeiro nome.

def Main022():
    nome = str(input('Nome completo: ')).strip()  
    print(nome.upper())
    print(nome.lower())
    print('Tamanho total:',len(nome)-nome.count(' '))
    nomeFatiado = nome.split()
    print(f'Primeiro nome tem {len(nomeFatiado[0])} ')

Main022()

#Lembrando que Strip() é para retirar os espaços que colocar a mais.
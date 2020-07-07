#04 Destrinchar o valor de uma variável. 

def Main004():
    anything = input('Digite algo: ')
    print('O tipo é: ', type(anything))
    print('Só tem espaços? ', anything.isspace())
    print('É um número? ', anything.isnumeric())
    print('É alfabético? ', anything.isalpha())
    print('Éalfanumérico? ', anything.isalnum())
    print('Está em maiúsculas? ', anything.isupper())
    print('Está em minúsculas? ', anything.islower())
    print('Está capitalizada? ', anything.istitle())

Main004()

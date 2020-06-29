# Faça um programa que some os primeiros n números primos de uma sequencia (1 a infinito).

def Main():
    somapr = 0; conf = 0; numc = 1; num = 0
    n = int(input('Digite os n primeiros primos a serem somados: '))
    while True:        
        print(10*'-')
        print(f'Vez do {numc}')

        for m in range (1, numc+1):
            print(f'numc: {numc}, divisor:{m}')
            if numc%m == 0:
                conf += 1
            print(f'conf: {conf}')

        if conf == 2 or conf == 1:
            print(f'{numc} é primo!')
            somapr += numc; num += 1
            print(f'soma:{somapr}')
        conf = 0; 
        numc += 1
        if num == n:
            break
    print('end')    

Main()


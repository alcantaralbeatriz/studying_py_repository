#63. Faça um programa que leia um número inteiro e mostre os n primeiros números da sequência de Fibonacci.

def Main063():
    n_elementos = int(input('Mostrar quantos elementos?'))
    contador = antecessor = 0
    num_n = 1
    print('0',end=' - ')

    while contador < (n_elementos-1):
        print(num_n, end=' - ')
        contador += 1
        sucessor = antecessor + num_n
        antecessor = num_n
        num_n = sucessor
    print('fim.')

Main063()
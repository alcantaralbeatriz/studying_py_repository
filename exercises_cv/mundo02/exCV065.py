#65. Faça um programa que leia vários números inteiros, pergunte ao usuário se ele quer continuar. Ao final, mostre a média dos valores, o maior e menor número.

def Main065():
    num_inteiro = int(input('Digite um número inteiro: '))
    resposta = str(input('Deseja continuar? [S-sim; N-não) ')).upper()
    qtdd_num = somatoria = 0
    todos_inteiros = [num_inteiro]
    somatoria += num_inteiro
    qtdd_num += 1
    
    while resposta == 'S':
        num_inteiro = int(input('Digite outro número inteiro: '))
        todos_inteiros.append(num_inteiro)
        somatoria += num_inteiro
        qtdd_num += 1
        resposta = str(input('Deseja continuar? [S-sim; N-não) ')).upper()
    
    todos_inteiros.sort()
    media = somatoria/qtdd_num; maior = todos_inteiros[qtdd_num - 1]; menor = todos_inteiros[0]

    if resposta == 'N':
        print(f'Média: {media:.2f}; Maior: {maior}; Menor: {menor}')

Main065()
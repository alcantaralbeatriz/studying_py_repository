#59. Faça um programa que leia dois números e forneça um menu de opções parao usuário escolher se quer somar, multiplicar, dizer qual o maior, fornecer novos números, ou sair do programa.

def Main059():
    valor_a = int(input('Primeiro valor inteiro: '))
    valor_b = int(input('Segundo valor inteiro: '))
    opcao = 0
    while opcao != 5:
        print('''Qual sua opção?
                [1] somar
                [2] multiplicar
                [3] maior
                [4] novos números
                [5] sair do programa''')
        opcao = int(input('Qual é a sua opção?'))
        if opcao == 1:
            print(f'A soma entre {valor_a} e {valor_b} é {valor_a + valor_b}!')
        elif opcao == 2:
            print(f'A multiplicação entre {valor_a} e {valor_b} é {valor_a * valor_b}!')
        elif opcao == 3:
            if valor_a > valor_b:
                print(f'O maior número é {valor_a}!')
            elif valor_b > valor_a:
                print(f'O maior número é {valor_b}!')
        elif opcao == 4:
            valor_a = int(input('Primeiro valor inteiro: '))
            valor_b = int(input('Segundo valor inteiro: '))
        elif opcao not in [1, 2, 3, 4, 5]:
            print('Opção inválida! Escolha novamente:')
        
    print('Fim!')

Main059()
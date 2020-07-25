#44. Faça um programa que calcule o valor a ser pago por um produto, considerando o preço normal e a condição de pagamento. 1 - à vista em dinheiro (10% de desconto); 2 - à vista no débito (5% desconto); 3 - 2x no cartão (preço normal); 4 - 3x ou mais no cartão (20% de juros).

def Main044():
    valor = int(input('Digite o valor do produto: R$ '))
    print('Agora escolha a opção de pagamento: \n\033[1;31m1\033[m - À vista dinheiro/cheque')
    print('\033[1;33m2\033[m - À vista cartão \n\033[1;35m3\033[m - Até 2x no cartão')
    print('\033[1;36m4\033[m - 3x ou mais no cartão')
    forma_pagamento = int(input('Opção de pagamento:'))
    if forma_pagamento == 1:
        print(f'O valor a ser pago será R$ {valor * 0.9:.2f}.')
    elif forma_pagamento == 2:
        print(f'O valor a ser pago será R$ {valor * 0.95:.2f}.')
    elif forma_pagamento == 3:
        print(f'O valor a ser pago será R$ {valor:.2f}, em 2x de R$ {valor * 0.5:.2f}.')
    elif forma_pagamento == 4:
        num_parcelas = int(input(f'Em quantas vezes? Número de parcelas:'))
        valor_parcela = (valor * 1.2) / num_parcelas
        print(f'O valor a ser pago será R$ {valor * 1.2:.2f}, em {num_parcelas}x de R$ {valor_parcela:.2f}.')
    else:
        print('Opção inválida!')

Main044()
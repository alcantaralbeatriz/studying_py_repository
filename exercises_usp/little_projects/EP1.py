
def numeracao_meses(): #Para esclarecer ao usuario a numeracao a ser utilizada.
    print('Considere os seguintes numeros para os respectivos meses:\n'
    '[1] - Janeiro    [7]  - Julho\n[2] - Fevereiro  [8]  - Agosto\n'
    '[3] - Março      [9]  - Setembro\n[4] - Abril      [10] - Outubro\n'
    '[5] - Maio       [11] - Novembro\n[6] - Junho      [12] - Dezembro')

def proporcao_apos_meses(ma, mf, pa):
    float(pa)
    cm = 0
    while cm < mf:
        if ma in (12, 1, 2):
            rm = 3.65
        elif ma in (6, 7, 8):
            rm = 3.3
        elif ma in (3, 4, 5, 9, 10, 11):
            rm = 3.5

        ps = float(rm * pa * (1 - pa))
        pa = ps

        if ma == 12:
            ma = 0
        ma += 1; cm += 1

    return ps

def main():
    proporcao_atual = input('Entre com a proporcao atual: ').replace(',','.')
    numeracao_meses()
    mes_atual = int(input('Entre com o mes atual: '))
    meses_futuros = int(input('Entre com o numero de meses no futuro: '))

    proporcao_nova = proporcao_apos_meses(mes_atual, meses_futuros, proporcao_atual)

    print(f'A proporção após {meses_futuros} meses é: {proporcao_nova:.4f}')

main()
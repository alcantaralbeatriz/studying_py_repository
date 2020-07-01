
def Nummes(): #Para esclarecer ao usuario a numeracao a ser utilizada.
    print('Considere os seguintes numeros para os respectivos meses:')
    print('[1] - Janeiro    [7]  - Julho\n[2] - Fevereiro  [8]  - Agosto')
    print('[3] - Março      [9]  - Setembro\n[4] - Abril      [10] - Outubro')
    print('[5] - Maio       [11] - Novembro\n[6] - Junho      [12] - Dezembro')

def main():
    proporcao_atual_1 = input('Entre com a proporcao atual: ').replace(',','.')
    proporcao_atual_2 = float(proporcao_atual_1)
    Nummes()
    mes_atual = int(input('Entre com o mes atual: '))
    mf = int(input('Entre com o numero de meses no futuro: '))
    ms = mf; cm = rm = 0

#'cm' e para a contagem de meses.
#'mf' e para o calculo sem afetar 'ms'.
#'rm' e para calcular o coeficiente que varia conforme o mes do ano.

# Proporcao da populacao em relacao a populacao maxima apos {dm} meses.
while cm < ms:
    if mes_atual in (12, 1, 2):
        rm = 3.65
    elif mes_atual in (6, 7, 8):
        rm = 3.3
    elif mes_atual in (3, 4, 5, 9, 10, 11):
        rm = 3.5
    ps = float(rm * proporcao_atual_2 * (1 - proporcao_atual_2))
    proporcao_atual_2 = ps
    if mes_atual == 12:
        mes_atual = 0
    mes_atual += 1; cm += 1

print(f'A proporção após {mf} meses é: {ps:.4f}')

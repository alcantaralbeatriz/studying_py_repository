

# `n` menor que 0; soma das distribuições diferente de 1; `µ` fora do intervalo [0, 1]; `ε` negativo.

def verificaEntrada(n, di0, di1, di2, mu, ep):
    sum_distributions = di0 + di1 + di2
    while sum_distributions != 1 or n < 0 or (mu < 0 and mu > 1) or ep <= 0:
        sum_distributions = di0 + di1 + di2

        if sum_distributions != 1:
            print('Erro: soma das distribuicoes eh diferente de 1.')
            n, di0, di1, di2, mu, ep = chamaEntradas() 

        if n < 0:
            print('Erro: n (numero de geracoes) não pode ser negativo.')
            n, di0, di1, di2, mu, ep = chamaEntradas()

        if mu < 0 and mu > 1:
            print('Erro: mu (fator de ponderacao) não pode ser fora do intervalo [0, 1].')
            n, di0, di1, di2, mu, ep = chamaEntradas()

        if ep <= 0:
            print('Erro: n (numero de geracoes) não pode ser negativo.')
            n, di0, di1, di2, mu, ep = chamaEntradas()

    return n, di0, di1, di2, mu, ep
    
def quadroPunnet():
# dado os índices dos genótipos de ambos os pais e do filho, retorne a probabilidade do filho ser gerado de acordo com o quadro de Punnett. Atribuindo 0 para BB, 1 para Bb, e 2 para bb.


#recebe os índices dos genótipos de ambos os pais e do filho e as distribuições de cada genótipo e calcula a probabilidade de um filho com aquele genótipo nascer na próxima geração.
def calculaProbabilidadeFilho():


def chamaEntradas():
    n_generation = int(input('Número de gerações (n): ')

    di_BB= float(input('Distribuição de BB: ')
    # Distribuicao inicial de BB (homozigoto dominante)

    di_Bb= float(input('Distribuição de Bb: ')
    # Distribuicao inicial de Bb (heterozigoto)

    di_bb= float(input('Distribuição de bb: ')
    # Distribuicao inicial de bb (homozigoto recessivo)

    mu = float(input('Valor do fator de ponderacao (mu): '))

    epsilon = float(input('Valor do limiar (epsilon): '))

    return n_generation, di_BB, di_Bb, di_bb, mu, epsilon

def main():
    n, di0, di1, di2, mu, ep = chamaEntradas()

    verificaEntrada(n, di0, di1, di2, mu, ep)



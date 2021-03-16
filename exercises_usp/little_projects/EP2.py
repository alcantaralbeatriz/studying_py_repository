def VarDistr():
    # Distribuicao inicial de BB (homozigoto dominante)
    di_BB = input('Distribuição de BB: ').replace(',', '.'); di_BB = float(di_BB)

    # Distribuicao inicial de Bb (heterozigoto)
    di_Bb = input('Distribuição de Bb: ').replace(',', '.'); di_Bb = float(di_Bb)

    # Distribuicao inicial de bb (homozigoto recessivo)
    di_bb = input('Distribuição de bb: ').replace(',', '.'); di_bb = float(di_bb)

    # Verificacao de entradas:
    while di_BB > 1 or di_BB < 0:
        print('Erro: dBB nao estah entre 0 e 1.')
        di_BB = input('Distribuição de BB: ').replace(',', '.'); di_BB = float(di_BB)
    while di_Bb > 1 or di_Bb < 0:
        print('Erro: dBb nao estah entre 0 e 1.')
        di_Bb = input('Distribuição de Bb: ').replace(',', '.'); di_Bb = float(di_Bb)
    while di_bb > 1 or di_bb < 0:
        print('Erro: dbb nao estah entre 0 e 1.')
        di_bb = input('Distribuição de bb: ').replace(',', '.'); di_bb = float(di_bb)

    return di_BB, di_Bb, di_bb

#Verificacao de entradas:
def verificaEntrada(n, mu, eps):   
    while n < 0:
        print('Erro: n (numero de geracoes) precisa ser um numero inteiro e positivo.')
        n = input('Digite n: '); n = int(n)

    while eps < 0:
        print('Erro: epsilon precisa ser um numero positivo.')
        eps = input('Digite epsilon: ').replace(',', '.'); eps = float(eps)

    while mu < 0 or mu > 1:
        print('Erro: mu precisa ser um numero positivo e menor que 1.')
        mu = input('Digite mu: ').replace(',', '.'); mu = float(mu)

    return n, mu, eps

#Somatória das probabilidades dos novos possíveis descendentes:
def Distr_nova(a, b, c):
    dn_BB = (a * a) + (a * b) + (0.25 * b * b)
    dn_Bb = (a * b) + (0.5 * b * b) + (2 * a * c) + (b * c)
    dn_bb = (c * c) + (b * c) + (0.25 * b * b)
    return dn_BB, dn_Bb, dn_bb

#Nova distribuição considerando descendentes e geração inicial:
def Distr_final(dn_BB, dn_Bb, dn_bb, mu, di_BB, di_Bb, di_bb):
    A = (mu * di_BB) + ((1 - mu) * dn_BB)
    B = (mu * di_Bb) + ((1 - mu) * dn_Bb)
    C = (mu * di_bb) + ((1 - mu) * dn_bb)
    return A, B, C

def SomaEpsilon(di_BB, df_BB, di_Bb, df_Bb, di_bb, df_bb, eps):
    s0 = df_BB - di_BB
    s1 = df_Bb - di_Bb
    s2 = df_bb - di_bb

    if s0 < 0:
        s0 = s0 * (-1)
    if s1 < 0:
        s1 = s1 * (-1)
    if s2 < 0:
        s2 = s2 * (-1)

    somaeps = s0 + s1 + s2
    return somaeps

def main():

    n = input('Número de gerações (n): '); n = int(n)

    mu = input('Valor do fator de ponderacao (mu): ').replace(',', '.'); mu = float(mu)

    eps = input('Valor do limiar (epsilon): ').replace(',', '.'); eps = float(eps)

    verificaEntrada(n, mu, eps)

    di_BB, di_Bb, di_bb = VarDistr()

    soma_dist = di_BB + di_Bb + di_bb
    while soma_dist != 1.0:
        print('Erro: Soma das distribuições eh diferente de 1.')
        d0, d1, d2 = VarDistr()
        soma_dist = d0 + d1 + d2

    cont = 1; m = int(n + 1)

    while cont < m:
        dn_BB, dn_Bb, dn_bb = Distr_nova(di_BB, di_Bb, di_bb)

        df_BB, df_Bb, df_bb = Distr_final(dn_BB, dn_Bb, dn_bb, mu, di_BB, di_Bb, di_bb)

        print(f'Ciclo {cont+1}: dBB = {df_BB:.3f} -- dBb = {df_Bb:.3f} -- dbb = {df_bb:.3f}')

        SomaEpsilon(di_BB, df_BB, di_Bb, df_Bb, di_bb, df_bb, eps)

        di_BB, di_Bb, di_bb = df_BB, df_Bb, df_bb

        cont += 1


main()
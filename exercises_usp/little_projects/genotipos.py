
def VarDistr():
    a = input('Digite dZZ: ').replace(',', '.'); a = float(a)
    b = input('Digite dZz: ').replace(',', '.'); b = float(b)
    c = input('Digite dzz: ').replace(',', '.'); c = float(c)
    return a, b, c

def verificaEntrada(n, a, b, c, mu, eps):
    while n < 0:
        print('Erro: n precisa ser um numero inteiro e positivo, sem ponto ou virgula.')
        n = int(input('Digite n: '))

    while a > 1 or a < 0:
        print('Erro: dZZ nao estah entre 0 e 1')
        a = input('Digite dZZ: ').replace(',', '.'); a = float(a)
    while b > 1 or b < 0:
        print('Erro: dZz nao estah entre 0 e 1')
        b = input('Digite dZz: ').replace(',', '.'); b = float(b)
    while c > 1 or c < 0:
        print('Erro: dzz nao estah entre 0 e 1')
        c = input('Digite dzz: ').replace(',', '.'); c = float(c)

    tot = a + b + c
    while tot != 1.0:
        print('Erro: Soma das distribuições eh diferente de 1')
        a,b,c = VarDistr()
        tot = a + b + c

    while eps < 0:
        print('Erro: epsilon precisa ser um numero positivo.')
        eps = int(input('Digite epsilon: '))

    return n, a, b, c, mu, eps

def Distr(a, b, c):
    TZZ = (a * a) + (a * b) + (0.25 * b * b)
    TZz = (a * b) + (0.5 * b * b) + (2 * a * c) + (b * c)
    Tzz = (c * c) + (b * c) + (0.25 * b * b)
    return TZZ, TZz, Tzz

def novaDistr(TZZ, TZz, Tzz, mu, a, b, c):
    A = (mu * a) + ((1 - mu) * TZZ)
    B = (mu * b) + ((1 - mu) * TZz)
    C = (mu * c) + ((1 - mu) * Tzz)
    return A, B, C

def Main():
    n = input('Digite n: '); n = int(n)
    a,b,c = VarDistr()
    # fator de ponderação
    mu = input('Digite mu: ').replace(',', '.'); mu = float(mu)
    # fator de parada
    eps = input('Digite epsilon: ').replace(',', '.'); eps = float(eps)
    verificaEntrada(n, a, b, c, mu, eps)
    cont = 1

    while cont < n+1:
        TZZ, TZz, Tzz = Distr(a,b,c)
        a, b, c = novaDistr(TZZ, TZz, Tzz, mu, a, b, c)
        somaeps = (TZZ - a) + (TZz - b) + (Tzz - c)
        print(f'Ciclo {cont}: dZZ = {a:.3f} -- dZz = {b:.3f} -- dzz = {c:.3f}')
        cont += 1
        if somaeps < eps:
            break

Main()
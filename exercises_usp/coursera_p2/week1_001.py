def cria_matriz(num_linhas, num_colunas, valor):
    '''(int, int)
    ->Esta função cria uma matriz com elementos de mesmo valor.
    :param num_linhas: número de linhas da matriz
    :param num_colunas: número de colunas da matriz
    :param valor: valor de todos os elelmentos da matriz
    :return: retorna matriz
    '''
    matriz = []
    for x in range(num_linhas):
        linha = []
        for y in range(num_colunas):
            linha.append(valor)
        matriz.append(linha)
    return matriz

#teste
#matrizao = cria_matriz()
#print(matrizao)

def mostra_matriz(matriz_dada):
    '''(list)
    -> Esta função mostra a matriz fornecida mais legível ao ser humano.
    :param matriz_dada: matriz fornecida
    :return: sem return
    '''
    for x in range(0,len(matriz_dada)):
        print('|',end='')
        for y in range(0,len(matriz_dada[x])):
            print(f'{matriz_dada[x][y]:^3}',end='')
        print('|')

#teste
# matrizao = [[1,2,3],[4,5,6],[7,8,9]]
#mostra_matriz(matrizao)

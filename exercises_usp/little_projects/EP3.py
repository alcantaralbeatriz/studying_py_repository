########################################################
# MAC0119 ICB-IME                                      #
# Prof. Roberto Cesar                                  #
#                                                      #
# Terceiro Exercicio Programa -- Massas de proteinas   #                 #
#                                                      #
# Beatriz Alcantara Leite numero USP.8034656           #
#                                                      #
# Informacoes sobre o Desenvolvimento:                 #
# Ambiente PyCharm                                     #
# Sistema Operacional Windows                          #
########################################################

def raw_input():  #funcao raw_input para requisitar o arquivo ao usuario
    #nomearquivo = input('Qual o nome do arquivo? ')
    nomearquivo = 'proteina.fasta'
    arquivo = open(nomearquivo)
    conteudo = arquivo.read()
    arquivo.close()
    linhas = conteudo.split('\n')
    proteina=[]

    for x in linhas:
        if '>' in x:
            prot = []
            prot.append(x)
        else:
            prot.append(x)
            prot.append(float(weight(x)))
            proteina.append(prot)
    return proteina

def weight(x):
    pesosAA = [['A', 71.037], ['R', 156.101], ['N', 114.042], ['D', 115.026],
               ['C', 103.009], ['E', 129.042], ['Q', 128.058], ['G', 57.021],
               ['H', 137.058], ['I', 113.084], ['L', 113.084], ['K', 128.094],
               ['M', 131.040], ['F', 147.068], ['P', 97.052], ['S', 87.032],
               ['T', 101.047], ['W', 186.079], ['Y', 163.063], ['V', 99.068]]
    pesot = 0
    for y in range(len(x)):
        for w in range(len(pesosAA)):
            if x[y] == pesosAA[w][0]:
                pesot += pesosAA[w][1]
    return float(pesot)

def ordemCres(proteina):
    for x in range(len(proteina)):
        min = proteina[x][2]
        for y in range(x+1,len(proteina)):
            if proteina[y][2]<proteina[x][2]:
                min=proteina[y][2]
                proteina[y], proteina[x] = proteina[x], proteina[y]
    return proteina

def impressao(prots): #impressao das proteinas em ordem crescente
    print(f'{"Peso":<10}{"Descrição":<15}{"Sequencia":<50}')
    for w in range(len(prots)):
        print(f'{prots[w][2]:.4f}  {prots[w][0]:<15}{prots[w][1]:<50}')

def main():
    prots = ordemCres(raw_input())
    impressao(prots)

main()
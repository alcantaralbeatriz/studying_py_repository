def raw_input():
    #nome_arquivo = str(input('Nome do arquivo: '))
    arquivo = open('proteinass.fasta')
    conteudo = arquivo.read(); 
    arquivo.close()
    linhas = conteudo.split('\n')
    proteinas=[]

    for x in linhas:
        if '>' in x:
            prot = []
            prot.append(x)
        else:
            prot.append(x)
            prot.append(float(weightMass(x)))
            proteinas.append(prot)

    return proteinas

def weightMass(aa_proteina):
    pesosAA = [['A', 71.037], ['R', 156.101], ['N', 114.042], ['D', 115.026],
               ['C', 103.009], ['E', 129.042], ['Q', 128.058], ['G', 57.021],
               ['H', 137.058], ['I', 113.084], ['L', 113.084], ['K', 128.094],
               ['M', 131.040], ['F', 147.068], ['P', 97.052], ['S', 87.032],
               ['T', 101.047], ['W', 186.079], ['Y', 163.063], ['V', 99.068]]
    peso_total = 0
    for y in range(len(aa_proteina)):
        for w in range(len(pesosAA)):
            if aa_proteina[y] == pesosAA[w][0]:
                peso_total += pesosAA[w][1]
    return float(peso_total)

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
    inicio = raw_input()
    proteinasAnalisadas = ordemCres(inicio)
    impressao(proteinasAnalisadas)

main()
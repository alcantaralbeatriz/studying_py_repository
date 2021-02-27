def leRatinho():
	massa = float(input('massa: '))
	tipo = int(input('tipo 1 e 2: '))
	dias = int(input('dias: '))
	return(massa, tipo, dias)

def calculaMassa(massa0, taxa, dias):
	m = massa0
	for i in range(dias): 
		m += taxa * m
	return(m)

def main():
	n = int(input('n: '))
	x = float(input('taxa (%): '))
	x = x / 100
	somaMassaA = somaMassaB = nRatinhosA = nRatinhosB = 0
	for i in range(n):
		massa, tipo, dias = leRatinho()
		massaFinal = calculaMassa(massa, x, dias)
	if (tipo == 1):
		nRatinhosA += 1
		somaMassaA += massaFinal
	else:
		nRatinhosB = nRatinhosB + 1
		somaMassaB += massaFinal
	print('A: ', somaMassaA/nRatinhosA)
	print('B: ', somaMassaB/nRatinhosB)

main()
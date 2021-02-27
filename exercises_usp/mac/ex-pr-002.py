def invertePalavra(s):
	palavraInvertida = []
	cont = len(s)-1
	while cont >= 0:
		palavraInvertida.append(s[cont])
		cont -= 1
	return(palavraInvertida)
def main():
	frase = input('Frase: ')
	frase = list(frase)
	cont = 0
	palavra = []
	while cont < len(frase):
		if (frase[cont] != ' '):
			palavra.append(frase[cont])
			cont += 1
		else:
			palavra = invertePalavra(palavra)
			print(''.join(palavra), end=' ')
			palavra = []
			cont += 1
main()
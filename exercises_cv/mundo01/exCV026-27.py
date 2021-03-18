#26. Faça um programa que leia uma frase e mostre: quantas vezes aparece a letra 'a'; em que posição ela aparece a primeira e ultima vez.

#27. Faça um programa que leia o nome completo e mostre o primeiro e ultimo nome separadamente. 

def Main026():
    frase = str(input('Frase: ')).strip().lower()
    print('Tem {} vezes a letra A.'.format(frase.count('a')))
    print('Primeiro na posição {}.'.format(frase.find('a')+1))
    print('Último na posição {}.'.format(frase.rfind('a')+1))

def Main027():
    nome = input('Qual seu nome completo?').strip().split()
    print('Primeiro nome:', nome[0].capitalize())
    print('Último nome: ', nome[len(nome)-1].capitalize())

Main027()
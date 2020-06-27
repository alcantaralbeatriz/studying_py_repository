#1 Criar um programa que escreva "Hello world!".

#print("Hello world!")


#2 Criar programa que leia o nome do usuário e mostra uma msg de boas-vindas

def Main002():
    nome = str(input('Qual o seu nome? '))
    print(f'Seja Bem-Vindx {nome}!')

#Main002()


#3 Criar um programa que leia dois números e mostre a soma entre eles.

def Main003():
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    print(f'A soma de {n1} e {n2} é {(n1+n2):.2f}.')


Main003()



def Main00x():
    print('Qual a data do seu nascimento?')
    b = int(input('Dia:'))
    c = str(input('Mês (escrito):'))
    d = int(input('Ano (número):'))
    print(f'Você nasceu no dia {b} de {c} de {d}')
    
#Main00x()
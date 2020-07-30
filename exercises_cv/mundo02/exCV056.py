#56. Faça um programa que leia, de quatro pessoas, o nome, idade e sexo, então forneça a idade média do grupo, o numero de mulheres com menos de 20 anos e o nome do homem mais velho.

def Main056():
    nomes = []; mais_velho = 0; nome_mais_velho = ''
    idades = []; somatoria = 0
    sexos = []; mulheres_menores = 0

    for x in range(1,3):
        print(f'{x}ª pessoa')
        nome = input('Nome: ').capitalize(); nomes.append(nome)

        sexo = input('Sexo [M/F]: ').upper()
        if sexo not in ['M','F']:
            while sexo not in ['M','F']:
                sexo = input('Digite M ou F. Sexo [M/F]: ').upper()
            sexos.append(sexo)
        else:
            sexos.append(sexo)

        idade = int(input('Idade: '))
        idades.append(idade)

        somatoria += idade
        if idade < 20 and sexo == 'F':
            mulheres_menores += 1
        
        if idade > mais_velho and sexo == 'M':
            nome_mais_velho = nome
            mais_velho = idade
        
    print(nomes, idades, sexos)
    print(f'A média de idade do grupo é {somatoria/(len(idades)):.1f}.')
    print(f'A quantidade de mulheres com menos de 20 anos é {mulheres_menores}.')
    print('O homem mais velho é o {} de {} anos'.format(nome_mais_velho, mais_velho))



Main056()
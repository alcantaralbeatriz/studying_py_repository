def LeiaA(fr,car):
    cont = 0
    for x in range(0,len(fr)):
        y = fr[x]
        mai = car.upper()
        min = car.lower()
        if y == mai or y == min:
            cont += 1
    return cont

def main():
    f = input('Qual sua string/palavra? ')
    c = input('Qual o caracter que irei contar?')
    print(f'A palavra {f} tem {LeiaA(f,c)} letra(s) {c}.')

main()

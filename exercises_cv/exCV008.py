#8 Faça um programa que leia uma medida em metros e converta-a em km,hm,dam,dm,cm,mm.

def Main008():
    m = float(input('Distância em metros: '))
    print(f'{m} metros são: {m*0.001}km, {m*0.01}hm, {m*0.1:.2f}dam.')
    print(f'{m} metros são: {m*10:.0f}dm, {m*100:.0f}cm, {m*1000:.0f}cm, {m*10000:.0f}mm.')


Main008()

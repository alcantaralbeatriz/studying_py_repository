#10 Faça um programa que converta real em dólar (R$5,5) e pesos argentinos (R$0,078).

def Main010():
    num = float(input('Quanto será convertido? '))
    print(f'R${num:.2f} são {num*0.18:.2f} dólares e {num*12.79:.2f} pesos argentinos.')

Main010()

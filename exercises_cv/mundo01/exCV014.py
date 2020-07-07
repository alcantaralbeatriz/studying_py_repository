#14. Faça um programa que converta uma temperatura digitada em Celsius para Fahrenheit e Kelvin.

def Main014():
    TempCelsius = float(input('Temperatura em Celsius:'))
    TempFah = (((9*TempCelsius)+160)/5)
    print(f'Em Fahrenheit: {TempFah} F°.\nEm Kelvin: {TempCelsius + 273} K°.')
# Desafio 14:
# Escreva um programa que converta uma temperatura digitada em graus Celsius e converta para graus Fahrenheit.

temp = int(input('Digite a temperatura: '))
tipo = str(input(
    'Digite o tipo da temperatura de origem: C (Celsius) ou F (Fahrenheit): ')).upper().strip()
if tipo == 'C':
    tempf = (temp * (9 / 5)) + 32
    print('A temperatura digitada em {:.1f} C é igual a {:.1f} F'.format(
        temp, tempf))
if tipo == 'F':
    tempc = (temp - 32) / (9 / 5)
    print('A temperatura digitada em {:.1f} F é igual a {:.1f} C'.format(
        temp, tempc))

# Desafio 8:
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Digite o valor em metros: '))
medida = input('Digite a medida desejada (km, hm, dam, dm, cm, mm): ')
if (medida == 'km'):
    print('{} m equivalem a {} km'.format(metros, (metros * 0.001)))
elif (medida == 'hm'):
    print('{} m equivalem a {} hm'.format(metros, (metros * 0.01)))
elif (medida == 'dam'):
    print('{} m equivalem a {} dam'.format(metros, (metros * 0.1)))
elif (medida == 'dm'):
    print('{} m equivalem a {} dm'.format(metros, (metros * 10)))
elif (medida == 'cm'):
    print('{} m equivalem a {} cm'.format(metros, (metros * 100)))
elif (medida == 'mm'):
    print('{} m equivalem a {} mm'.format(metros, (metros * 1000)))

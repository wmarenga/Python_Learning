"""
While / Else:
contadores
acumuladores

"""
contador = 1
acumulador = 1

while contador <= 100:
    print(f'Contador={contador} e Acumulador={acumulador}')

    acumulador += contador
    contador += 1
else:  # O else só será executa quando o while se tornar False
    while contador > 0:
        acumulador -= contador
        contador -= 1
        print(f'Contador={contador} e Acumulador={acumulador}')
print('Isso será executado.')

# Aplicacao de laco FOR sobre uma lista

repetir = 's'
fatura = []
total = 0

while repetir == 's':
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preco: '))

    fatura.append([produto, preco])
    total += preco

    repetir = input('Cadastro mais algum item? (S ou N): ').lower()

for i in fatura:
    print(i[0], ':', i[1])

print('O total da fatura e: ', total)

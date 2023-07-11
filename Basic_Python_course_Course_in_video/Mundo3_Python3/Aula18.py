"""
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
print(teste)
# galera.append(teste) - desta maneira estamos criando uma ligação entre as duas listas.
# galera.append(teste[:]) - Criamos uma cópia da lista interna, podendo ser alteradas isoladamente.
galera.append(teste.copy())
teste[0] = 'Maria'
teste[1] = 22
# galera.append(teste)
# galera.append(teste[:])
galera.append(teste.copy())
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
"""

galera = list()
dado = list()
totmai = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado.copy())
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmai} maiores e {totmenor} de idade.')

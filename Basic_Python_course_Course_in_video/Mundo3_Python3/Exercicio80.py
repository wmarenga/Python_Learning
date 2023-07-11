# Desafio 80:
# Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = []
n = 0
for n in range(0, 5):
    número = int(input('Digite um valor: '))
    if n == 0 or número > lista[-1]:
        lista.append(número)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if número <= lista[pos]:
                lista.insert(pos, número)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1
print('-='*40)
print(f'Os valores digitados em ordem foram {lista}')

# Desafio 85:
# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e
# ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

número = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° número: '))
    if valor % 2 == 0:
        número[0].append(valor)
        número[0].sort()
    else:
        número[1].append(valor)
        número[1].sort()
print('#'*40)
print(f'Os números pares são {número[0]}')
print(f'Os números ímpares são {número[1]}')

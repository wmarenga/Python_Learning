# Desafio 31:
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens de
# até 200 Km e R$ 0.45 para viagens mais longas.

dist = float(input('Digite a distância total da viagem (Km): '))
if dist <= 200:
    custoviagem = dist * 0.5
else:
    custoviagem = dist * 0.45
print('O total de Km é {:.0f} e o custo total da viagem é de R$ {:.2f}'.format(
    dist, custoviagem))
print('Boa Viagem!')

# Usando operador ternário ou if in line (simplificado).

dist = float(input('Digite a distância total da viagem (Km): '))
custoviagem = dist * 0.5 if dist <= 200 else dist * 0.45
print('O total de Km é {:.0f} e o custo total da viagem é de R$ {:.2f}'.format(
    dist, custoviagem))
print('Boa Viagem!')

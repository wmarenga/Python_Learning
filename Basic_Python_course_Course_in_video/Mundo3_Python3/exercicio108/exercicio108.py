# Desafio 108:
# Adapte o código do desafio 107, criando uma função adicional
# chamada moeda() que consiga mostrar os valores como um valor
# monetário formatado.

import moeda


preço = float(input('Digite o preço '))
taxaaumento = int(input('Digite a taxa de aumento % '))
taxaredução = int(input('Digite a taxa de redução % '))
tipo = str(input('Digite o tipo de moeda: ')).strip().upper()[0:3]
# O primeiro "moeda" é o nome do módulo e o segundo "moeda" é o nome da função.
print(
    f'A metade de {tipo} {moeda.moeda(preço)} é {tipo} {moeda.moeda(moeda.metade(preço))}')
print(
    f'O dobro de {tipo} {moeda.moeda(preço)} é {tipo} {moeda.moeda(moeda.dobro(preço))}')
print(
    f'Aumentando {taxaaumento}%, temos {tipo} {moeda.moeda(moeda.aumentar(preço, taxaaumento))}')
print(
    f'Reduzindo {taxaredução}% temos {tipo} {moeda.moeda(moeda.diminuir(preço, taxaredução))}')

# Desafio 109:
# Modifique as funções que foram criadas no desafio 107 para que elas
# aceitem um parâmetro a mais, informando se o valor retornado por elas
# vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


from exercicio109 import moeda


preço = float(input('Digite o preço '))
taxaaumento = int(input('Digite a taxa de aumento % '))
taxaredução = int(input('Digite a taxa de redução % '))
tipomoeda = str(input('Digite o tipo de moeda: ')).strip().upper()[0:3]
# O primeiro "moeda" é o nome do módulo e o segundo "moeda" é o nome da função.
if tipomoeda == '':
    tipomoeda = 'R$'
else:
    tipomoeda = tipomoeda
print(
    f'A metade de {moeda.moeda(preço, tipomoeda)} é {moeda.metade(preço, tipomoeda)}')
print(
    f'O dobro de {moeda.moeda(preço, tipomoeda)} é {moeda.dobro(preço, tipomoeda)}')
print(
    f'Aumentando {taxaaumento}%, temos {moeda.aumentar(preço, taxaaumento, tipomoeda)}')
print(
    f'Reduzindo {taxaredução}% temos {moeda.diminuir(preço, taxaredução, tipomoeda)}')

# Desafio 15:
# Escreva um programa que pergunte a quantidade de Km percorridos por
# um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e
# R$ 0.15 por Km rodado.

km = float(input('Digite quantos Kms você percorreu (Km): '))
dias = int(input('Digite quantos dias alugou o carro (dias): '))
preco = (60 * dias) + (km * 0.15)
print('Você utilizou o carro por {} dias e o valor total a pagar é de R$ {:.2f}.'.format(dias, preco))

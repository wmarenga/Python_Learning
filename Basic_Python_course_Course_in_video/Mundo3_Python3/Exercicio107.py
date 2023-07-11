# Desafio 107:
# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobrar(), e metade().
# Faça também um programa que importe esse módulo e use algumas dessas
# funções.

from exercicio107 import moeda

# PROGRAMA PRINCIPAL
preço = float(input('Digite o preço R$ '))
print(f'A metade de R$ {preço:.2f} é R$ {moeda.metade(preço):.2f}')
print(f'O dobro de R$ {preço:.2f} é R${moeda.dobro(preço):.2f}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(preço, 10):.2f}')
print(f'Reduzindo 13% temos R$ {moeda.diminuir(preço, 13):.2f}')

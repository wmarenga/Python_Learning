# Desafio 110:
# Adicione o múdulo moeda.py criado nos desafios anteriores, uma função
# chamada resumo(), que mostre na tela algumas informações geradas pelas
# funções que já temos no módulo criado até aqui.

from exercicio110 import moeda


preço = float(input('Digite o preço: '))
moeda.resumo(preço, 20, 12, 'R$')

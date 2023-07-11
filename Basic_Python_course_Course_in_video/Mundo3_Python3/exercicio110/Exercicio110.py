# Desafio 110:
# Adicione o múdulo moeda.py criado nos desafios anteriores, uma função
# chamada resumo(), que mostre na tela algumas informações geradas pelas
# funções que já temos no módulo criado até aqui.

import moeda


preço = float(input('Digite o preço '))
taxaaumento = int(input('Digite a taxa de aumento % '))
taxaredução = int(input('Digite a taxa de redução % '))
moeda.resumo(preço, taxaaumento, taxaredução)

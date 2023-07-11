"""
Documentação:
https://docs.python.org/3/tutorial/modules.html
"""

# import vendas.calc_preco
# from vendas import calc_preco
from vendas.calc_preco import formata_preco, aumento, reducao
# from vendas.formata import preco
import vendas.formata.preco as formata

preco = 49.90
preco_com_aumento = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_com_aumento)
# print(formata_preco(preco_com_aumento))

preco_com_reducao = reducao(valor=preco, porcentagem=15, formata=True)
print(preco_com_reducao)
# print(formata_preco(preco_com_reducao))

print(formata.real(50))

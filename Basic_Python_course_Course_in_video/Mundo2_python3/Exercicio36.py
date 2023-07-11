# Desafio 36:
# Escreva um programa para aprovar o empréstimo bancário para a compra
# de uma casa. O Programa vai perguntar o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder
# 30% do salário ou então o empréstimo será negado.

v_casa = float(input('Digite o valor da casa: R$ '))
salário = float(input('Digite o seu último salário: R$): '))
anos = int(input('Digite em quantos anos quer pagar o empréstimo: '))
meses = 12 * anos
salário_possível = salário * 0.3
parcela_mensal = v_casa / meses
# Usamos o "end" para alinhar os dois print's um uma única linha.
# print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(
#     v_casa, anos), end='')
# print(' a prestação será de R$ {:.2f}'.format(parcela_mensal))
if parcela_mensal <= salário_possível:
    print('A sua parcela mensal é R$ {:.2f} e o empréstimo será pago em {} meses.'.format(
        parcela_mensal, meses))
    print('Seu empréstimo será \033[1;35;42mCONCEDIDO!\033[m')
else:
    print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de \033[1;33;41mR$ {:.2f}\033[m.'.format(
        v_casa, anos, parcela_mensal))
    print('Seu empréstimo foi \033[1;33;41mNEGADO!\033[m')

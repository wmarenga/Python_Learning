# Desafio 44:
# Elabore um programa que calcule o valor a ser pago por um
# produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
# 1) Á vista em DINHEIRO/ CHEQUE: 10% de desconto;
# 2) Á vista no cartão: 5% de desconto;
# 3) Em até 2x NO CARTÃO: preço normal;
# 4) 3x ou MAIS no cartão: 20% de juros.

# Para centralizar em 40 espaços usamos ^40.
print('{:=^40}'.format(' Lojas Guanabara '))
p = float(input('Digite o valor do produto (R$): '))
print("""
Selecione a condição de pagamento:
[1] Dinheiro ou Cheque - á vista (-10%)
[2] Cartão á vista (-5%)
[3] 2x no cartão (valor normal)
[4] 3x ou mais cartão (+20%)""")
cond = int(input('Selecione a forma de pagamento: '))
if cond == 1:
    pf = p * 0.9
    #print('O preço final com desconto de \033[1;32m10%\033[m é \033[1;32mR$ {:.2f}\033[m.'.format(pf))
elif cond == 2:
    pf = p * 0.95
    #print('O preço final com desconto de \033[1;32m5%\033[m é \033[1;32mR$ {:.2f}\033[m.'.format(pf))
elif cond == 3:
    #print('O preço final sem desconto é \033[1;32mR$ {:.2f}\033[m.'.format(p))
    pf = p
    parc = p / 2
    print(
        'Sua compra será parcelada em 2x de \033[7;32mR$ {:.2f}\033[m no final'.format(parc))
elif cond == 4:
    pf = p * 1.2
    totparc = int(input('Informe quantas parcelas: '))
    parc = pf / totparc
    #print('O preço final com juros de 20% é \033[1;31mR$ {:.2f}\033[m.'.format(pf))
    print('Sua compra será parcelada em {}x de \033[7;32mR$ {:.2f}\033[m no final'.format(
        totparc, parc))
else:
    pf = p
    print('Digite um valor válido!')
print(
    'Sua compra de \033[1;31mR$ {:.2f}\033[m vai custar \033[7;32mR$ {:.2f}\033[m no final.'.format(p, pf))

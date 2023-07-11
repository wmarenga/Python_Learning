# Desafio 29:
# Escreva um programa que leia a velocidade de um carro.
# 1) Se o carro ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.
# 2) A multa vai custar R$ 7.00 por cada Km acima do limite.

vel = float(input('Digite a velocidade do carro (Km/h): '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Sua velocidade foi de {:.2f} Km/h!'.format(vel))
    print(
        "Você ultrapassou o limite de velocidade declear 80 Km/h, \033[1;30;41mVOCÊ FOI MULTADO!!!\033[m")
    print('O valor da multa a ser paga é {:.2f} R$'.format(multa))
else:
    print('Sua velocidade foi de {:.2f} Km/h!'.format(vel))
    print('PARABÉNS!!! A sua velocidade está abaixo do limite permitido de 80 Km/h.')
print('Dirija com prudência!!')

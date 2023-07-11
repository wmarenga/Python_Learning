# Desafio 40:
# Crie um programa que leia duas notas de um aluno e
# calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# - Mádia abaixo de 5.0: Reprovado;
# - Média entre 5.0 e 6.9: Recuperação;
# - Média 7.0 ou superior: Aprovado.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
if média < 5:
    print('Sua média foi \033[1;31m{:.1f}\033[m.'.format(média))
    print('\033[1;33;41mVOCÊ FOI REPROVADO!\033[m')
elif 5 <= média < 7:
    print(média)
    print('Sua média foi \033[7;33m{:.1f}\033[m.'.format(média))
    print('\033[7;33mVOCÊ FICOU EM RECUPERAÇÃO!\033[m')
elif média >= 7:
    print('Sua média foi {:.1f}.'.format(média))
    print('\033[7;32mPARABÉNS! VOCÊ FOI APROVADO!\033[m')

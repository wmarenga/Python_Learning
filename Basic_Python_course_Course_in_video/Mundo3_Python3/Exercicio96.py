# Desafio 96:
# Faça um programa que tenha uma FUNÇÃO chamada área(),
# que receba as dimensões de um terreno retangular(largura e
# comprimento) e mostre a área do terreno.

def cabeçalho():
    print('-'*30)
    print('    CONTROLE DE TERRENOS     ')
    print('-'*30)


def área(l, c):
    área = l * c
    print(f'A largura é {l} (m) e o comprimento é {c} (m): ')
    print(f'Com as medidas fornecidas a área é {área}m2.')


cabeçalho()
área(l=float(input('Digite a largura do terreno: ')),
     c=float(input('Digite o comprimento do terreno: ')))

# Desafio 89:
# Crie um programa que leia nome e duas notas de vários alunos e
# guarde tudo em uma lista composta. No final, mostre um boletim
# contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.

cadastro = []
aluno = []
nota1 = 0
nota2 = 0
média = 0

while True:
    aluno = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    média = (nota1 + nota2) / 2
    cadastro.append([aluno, [nota1, nota2], média])
    decisão = str(input('Quer continuar? [S/N] ')).strip().upper()
    if decisão in 'Nn':
        break
    if decisão not in 'SsNn':
        decisão = str(
            input('Digite uma opção válida! [S/N]: ')).strip().upper()
print()
print('-='*40)
print(f'{"No.":<4}{"Nome":<12}{"Média":>8}')
print('-'*26)
for i, a in enumerate(cadastro):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar nota de qual aluno? (999 -> fim) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(cadastro) - 1:
        print(f'Notas de {cadastro[opc][0]} são {cadastro[opc][1]}')
    else:
        print('Digite uma opção válida!')
    print('<<< VOLTE SEMPRE >>>')

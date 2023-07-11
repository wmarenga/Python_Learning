# Desafio 7:
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
média = (nota1 + nota2) / 2
print('A média entre {} e {} é {:.1f}'.format(nota1, nota2, média))
if média >= 7:
    print('Você foi aprovado')
else:
    print('Você foi reprovado')

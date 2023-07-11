# Desafio 57:
# Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores
# 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até um valor correto.

sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')
               ).strip().upper()[0]
if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'
print('Sexo {} registrado com sucesso.'.format(sexo))

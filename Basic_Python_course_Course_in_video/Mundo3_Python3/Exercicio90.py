# Desafio 90:
# Faça um programa que leia nome e média de um aluno, guardando
# também a situação em um dicionário. No final, mostre o conteúdo
# da estrutura na tela.
cadastro = dict()
cadastro['aluno'] = str(input('Digite o nome do aluno: ')).strip().capitalize()
cadastro['média'] = float(input('Digite a média do aluno: '))

print('-~'*30)
print(f'Seu nome é {cadastro["aluno"]}.')
print(f'Sua média foi {cadastro["média"]:.1f}.')
if cadastro['média'] < 5:
    cadastro['situação'] = 'Reprovado'
    print(
        f'O {cadastro["aluno"]} foi \033[7;31m{cadastro["situação"]}!\033[m')
elif cadastro['média'] < 7:
    cadastro['situação'] = 'Recuperação'
    print(
        f'O {cadastro["aluno"]} ficou em \033[7;33;41m{cadastro["situação"]}!\033[m')
else:
    cadastro['situação'] = 'Aprovado'
    print(
        f'PARABÉNS {cadastro["aluno"]} você está \033[7;32m{cadastro["situação"]}!\033[m')
print(cadastro)
print(cadastro.items())  # mostra a chave e o valor.
print(cadastro.values())  # mostra somente o valor.
print(cadastro.keys())  # mostra somente a chave.
print()
# Maneira do professor:
for k, v in cadastro.items():  # {k} é a chave e {v} é o valor.
    print(f'   - {k} é igual a {v}')

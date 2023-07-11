"""
Documentação:
https://docs.python.org/3/library/functions.html#open

# Criando um arquivo para leitura e escrita
file = open('89_criando_lendo_escrevendo_apagando_arquivos/abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)  # Volta o cursor para posição inicial
# Lendo o arquivo
print('Lendo Linhas: ')
print(file.read())

print('##################')
file.seek(0, 0)  # Volta o cursor para o início novamente
# Lendo linha a linha
print(file.readline(), end='')  # Não mandar a quebra de linha
print(file.readline(), end='')  # Não mandar a quebra de linha

print('##################')

file.seek(0, 0)  # Volta o cursor para o início novamente
print(file.readlines())  # Exibe uma lista com todas as linhas

file.close()  # É muito importante fechar sempre o arquivo.

# Utilizando o bloco try

from asyncore import write


try:
    file = open('89_criando_lendo_escrevendo_apagando_arquivos/abc.txt', 'w+')
    file.write('Linha')
    file.seek(0)
    print(file.read())
finally:
    file.close()

# Maneira mais Pythômica, pois abre e fecha o arquivo automaticamente
with open('89_criando_lendo_escrevendo_apagando_arquivos/abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())

# Somente lendo o conteúdo do arquivo (r)
with open('89_criando_lendo_escrevendo_apagando_arquivos/abc.txt', 'r') as file:
    print(file.read())

# Ativa a função de adicionar coisas no arquivo => append (a+)
with open('89_criando_lendo_escrevendo_apagando_arquivos/abc.txt', 'a+') as file:
    file.write('Outra Linha\n')
    file.seek(0)
    print(file.read())

# Removendo o arquivo
import os
os.remove('89_criando_lendo_escrevendo_apagando_arquivos/abc.txt')

"""
# Criando e manipulando arquivos json

import json

d1 = {
    'pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}
print(d1)

# Convertendo para json
d1_json = json.dumps(d1, indent=True)

with open('89_criando_lendo_escrevendo_apagando_arquivos/abc.json', 'w+') as file:
    file.write(d1_json)


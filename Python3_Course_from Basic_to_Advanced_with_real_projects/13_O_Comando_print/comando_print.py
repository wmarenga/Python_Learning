"""
O print é uma função interna do Python. A sua funcionalidade é
mostrar a informação passada entre parênteses ou por (f-strings).

Exemplo entre parênteses:
print(123456)
print('Oi')
# Por padrão, será adicionado um espaço após cada vírgula.
print('Luiz', 'Otávio', 'Outra Coisa')

# Se realizármos uma operação de soma, não teremos os espaços, pois
os parâmetros estão sendo concatenados.
print('Luiz'+'Otávio'+'Outra Coisa')

# Print com argumento nomeado (sep=) - Separador:

Na mesma linha:
print('Luiz', 'Otávio', sep='-')
print('João', 'e', 'Maria', sep='-')

Pulando linhas:
print('Luiz', 'Otávio', sep='-', end=' => ')
print('João', 'e', 'Maria', sep='-', end='')

print('Estou', 'aprendendo', 'Python', sep='-', end=' ')
print('isso é muito', 'legal', sep='-', end='')

Obs: O Python diferencia letras minúsculas de maiúsulas, sendo assim,
a função Print() não existe.

Exemplo com f-strings:
nome = 'Wellington'
print(f'Olá eu sou {nome}')

Exercício CPF:

Formatar o número de CPF (824.176.070-18) com print().

print('824', '176', '070', sep='.', end='-')
print('18')

Com f-string:
numero = '82417607018'
print(f'{numero[0:3]}.{numero[3:6]}.{numero[6:9]}-{numero[9:11]}')
"""

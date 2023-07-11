# Desafio 77:
# Crie um programa que tenha uma Tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('atitude', 'aprender', 'fazer', 'vencer', 'viajar', 'correr',
            'gostar', 'trabalho', 'castelo', 'programar', 'dormir', 'sapato', 'camisa')

# "p" representa os elementos da Tupla palavras.
for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    # Para as letras (vogais) na palavra "p", mostrar somente as vogais.
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

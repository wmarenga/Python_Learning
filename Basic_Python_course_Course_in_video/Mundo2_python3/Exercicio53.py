# Desafio 53:
# Crie um programa que leia uma frase qualquer e diga
# se ela é um PALÍNDROMO, desconsiderando os espaços.
# Ex: apos a sopa
# a sacada da casa
# a torre da derrota
# o lobo ama o bolo
# anotaram a data da maratona
frase = str(
    input('Digite uma frase para saber se é um palíndromo: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
# Outra maneira de fazer sem o FOR.
inverso = junto[::-1]
"""for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]"""
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

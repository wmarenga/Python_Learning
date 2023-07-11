"""
Ranges

- Precisamos conhecer o 'loop for' para usar os ranges.
- Precisamos conhecer o 'range' para trabalhar melhor com 'loops for'.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Forma geral:

range(valor_de_parada)

Obs.: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Exemplo Forma 1 (Sempre inicia em 0 e o range com valor final menos 1)
for num in range(11):
    print(num)

# Exemplo Forma 2 (Valor de início determinado pelo usuário no 'for' e valor final -1)
range(valor_de_inicio, valor_de_fim/ parada)
for num in range(1, 11):
    print(num)

# Exemplo Forma 3 (Valor de início determinado pelo usuário no 'for' e valor final -1 e passo/ intervalo será especificado pelo usuário.)
range(valor_de_inicio, valor_de_fim/ parada, passo)
for num in range(1, 11, 2):
    print(num)

# Exemplo Forma 4 (Inversa) - valor inicial depois o valor final (não incluso) e o intervalo de decréscimo.

# range(valor_inicio, valor_de_final, (-)passo)

for num in range(10, 0, -2):
    print(num)

# Para gerar uma lista:
lista = list(range(10))
"""


"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Iterar sobre diicionários

! Imprime as chaves
for chave in receita:
    print(chave)

! Imprime os valores
for chave in receita:
    print(receita[chave])

! Imprime as chaves e valores
for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

# Acessando as chaves:

print(receita.keys())  # exibe um dicionário de chaves.

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores.

print(receita.values())  # Exibe um dicionário de valores.

for valor in receita.values():
    print(valor)

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita.items())  # Gera um dicionário de ítens (chave, valor) em tuplas.

! Desempacotamento de dicionários

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho (Se os valores forem todos inteiros ou reais).

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""

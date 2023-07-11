"""
Exercicio Proposto:
Utilizar list comprehention (uma linha de código)

carrinho = []
carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

total = []
for produto in carrinho:
    total.append(produto[1])
print(sum(total))
"""

carrinho = []
carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

print(sum([p[1] for p in carrinho]))

# Soluçao do professor

# total = [(x, y) for x, y in carrinho]  # desempacotando os valores
# print(total)

# Pegando os preços em y
total = [(y) for x, y in carrinho]  # desempacotando os valores
print(total)

# Convertendo todos os valores para float e fazendo a soma
total = sum([float(y) for x, y in carrinho])  # desempacotando os valores
print(total)

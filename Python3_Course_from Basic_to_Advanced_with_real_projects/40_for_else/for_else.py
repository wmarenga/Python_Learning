"""
for / else em Python:

# Exemplos:

nomes = ['Luiz Otávio', 'Joãozinho', 'Maria']

for n in nomes:
    print(n)
    continue  # o print abaixo não será executado
    print(n)

# Iterando sobre uma lista e fazendo uma verificação
for n in nomes:
    # Verifica se uma determinada string começa com 'J'
    if n.startswith('J'):
        print('Começa com J', n)
    else:
        print('Não começa com J', n)


"""
nomes = ['Luiz Otávio', 'Joãozinho', 'Maria']

comeca_com_j = False
for n in nomes:
    # Irá servir tanto para maiúsculo quanto para minúsculo.
    if n.lower().startswith('j'):
        comeca_com_j = True

if comeca_com_j:
    print('Existe uma palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J.')

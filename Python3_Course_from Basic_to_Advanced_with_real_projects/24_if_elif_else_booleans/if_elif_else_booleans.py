"""
Condições IF, ELIF e ELSE:

if             => se
elif (else if) => e se
else           => então

# Exemplo de if:

if True:
    print('Verdadeiro.')
    num_1 = 2
    num_2 = 4
    print(num_1 + num_2)

if False:
    print('Verdadeiro.')

# Esta expressão será executada mesmo sem o if.
print('A minha expressão não é verdadeira.')

# Exemplo if, else:

if True:
    print('Verdadeiro')
else:
    print('Não é verdadeiro.')

# Exemplo if, elif, else:

if False:
    print('Verdadeiro.')
elif False:
    print('Agora é verdadeiro.')
    nome = input("Qual o seu nome? ")
    print(f'Seu nome é {nome}.')
elif True:
    print('Mais uma verdadeira.')
    print(22 + 22)
else:
    print('Não é verdadeiro.')
    print('Olá')

Obs: Será executada a primeira condição verdadeira. Se nenhuma for True,
será executado o else.
"""

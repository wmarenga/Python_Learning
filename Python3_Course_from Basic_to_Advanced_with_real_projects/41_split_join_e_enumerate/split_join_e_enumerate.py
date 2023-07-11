"""
Split, Join, Enumerate em Python:

- split     => Tem a função de dividir uma string (str);
- join      => Tem a função de juntar uma lista (str);
- Enumerate => Tem a função de enumerar elementos da lista (index, value).

string = 'O Brasil é o país do futebol, o Brasil é penta.'

# Criando uma lista de uma string (pelos espaços)
lista_1 = string.split(' ')  # pelos espaços em branco
print(lista_1)
lista_2 = string.split(',')
print(lista_2)

# Iterando sobre a lista 1:
for n in lista_1:
    print(n)

# Contando palavras
for n in lista_1:
    print(f'A palavra {n} apareceu {lista_1.count(n)}X na frase.')

Exemplo 2:

string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_1 = string.split(' ')

palavra = ''
contagem = 0
for n in lista_1:
    qtd_vezes = lista_1.count(n)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = n

print(f'A palavra que apareceu mais vezes é: {palavra} ({contagem}X)')

Exemplo:

string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista_1 = string.split(' ')

for n in lista_1:
    # Remove espaços do início e do final da string.
    print(n.strip().capitalize())

# Inserindo cada palavra de uma string em uma lista
string = 'O Brasil é penta.'
lista = string.split(' ')
print(lista)

# Criando uma string com os elementos de uma lista com (join)
string2 = ' '.join(lista)
print(string2)

"""
# Exemplo de enumerate (retorna tuplas):

string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    # valor e lista[indice] são idênticos
    print(indice, valor, lista[indice])

# Exemplo com lista dentro de lista

lista_2 = [[1, 'Luiz'], [3, 'João'], [5, 'Maria']]

for indice, nome in lista_2:
    print(indice, nome)

# Com enumerate:
lista_3 = ['Luiz', 'João', 'Maria']

for indice, nome in enumerate(lista_3):
    print(indice, nome)

# Desempacotamento

n1, n2, n3 = lista_3
print(n2)

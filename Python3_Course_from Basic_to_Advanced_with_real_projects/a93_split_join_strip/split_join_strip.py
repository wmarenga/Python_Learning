"""
Split and Join em Python:

- split     => Tem a função de dividir uma string (str);
- join      => Tem a função de juntar uma lista (str);

"""
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

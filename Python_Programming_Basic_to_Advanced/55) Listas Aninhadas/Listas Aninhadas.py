""" 
Listas Aninhadas (Nested lists):

- Algumas linguagens de programacao (C, Java, PHP) possuem uma estrutura de dados chamadas de arrays:
1) Unidimensionais (Arrays/ Vetores);
2) Multidimensionais (Matrizes);

Em Python nos temos as listas
numeros = [1, 2, 'b', 3.14, True]

Limitacoes em outras linguagens:
- O tamanho fixo;
- Tipo de dados (nao podemos misturar).

# Exemplos

listas = [[1, 2, 3],[4, 5, 6],[7, 8, 9]] # Matriz 3 x 3
print(listas)
print(type(listas))

# Como fazer para acessar os dados?
print(listas[0]) # Acessando a primeira lista dentro da lista [1, 2, 3] (linha um da matriz)
print(listas[0][1]) # Acessando o segundo elemento (chave) dentro da lista [1, 2, 3] >> 2 (linha um da coluna 2 da matriz)
print(listas[2][1]) # Acessando o segundo elemento (chave) dentro da lista [7,8, 9] >> 8 (linha 3 da coluna 2)

# Iterando com loops em uma lista aninhada
for l in listas:
    for num in l:
        print(num)

# Como utilizar List Comprehension em lista aninhadas
# De dentro para fora (da esquerda para direita)
# Atencao! Para cada for interno devemos adicionar mais colchetes []
[[print(num) for num in l] for l in listas]


"""

# Outros Exemplos

# Gerando um tabuleiro/ matrix 3 x 3

# Forma sem List Comprehension
lista = []
tabuleiro = []

for l in range(1, 4):
    lista.append(l)
    tabuleiro.append(lista)

print(tabuleiro)

# Forma com List Comprehension
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range (1, 4)]
print(velha)

# Gerando valor inicial
print([['*' for i in range(1, 4)] for j in range(1, 4)])
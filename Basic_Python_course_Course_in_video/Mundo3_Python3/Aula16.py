"""
Em TUPLAS utilizamos parênteses ().
As listas utilizam colchetes [].
Os dicionários utilizam chaves {}.

### TUPLAS SÃO IMUTÁVEIS ###
Quando tentamos atribuir um novo valor para um elemento de uma Tupla, apresenta este
ERRO: 'tuple' object does not support item assignment, pois é impossível alterar uma Tupla.
lanche[1] = 'Refrigerante'
print(lanche)

### Somente podemos alterar a Tupla inteira ###
lanche = 'hambúrguer', 'suco', 'pizza', 'pudim'
print(lanche)
('hambúrguer', 'suco', 'pizza', 'pudim')
lanche = 'Brazil', 'Paraguai'
print(lanche)
('Brasil', 'Paraguai')

lanche = 'hambúrguer', 'suco', 'pizza', 'pudim'
print(lanche)  # mostra a Tupla inteira.
print(lanche[0])  # mostra o elemento contido no índice 0, ('hambúrguer')
print(lanche[-1])  # mostra o primeiro elemento do final da Tupla.
print(lanche[1:3])  # do elemento 1 até o 2 segundo ('suco', 'pizza')
print(lanche[2:])  # Do elemento 2 até o final ('pizza', 'pudim')
# do início até o elemento 2 (ignorando o último), ('hambúrguer', 'suco')
print(lanche[:2])
print(lanche[-2:])  # mostra do -2 até o final ('pizza', 'pudim')
# mostra do início até o -2 (desconsiderando o -2), ('hambúrguer', 'suco')
print(lanche[:-2])

lanche = 'hambúrguer', 'suco', 'pizza', 'pudim', 'batata frita'

# Quando o programa não está em execução é possível mexer na Tupla.

# Maneira mais comum 1:
for comida in lanche:
    print(f'Eu vou comer {comida}')

# Outra maneira de fazer 2:
# for cont in range(0, len(lanche)):
#    print(cont)  # mostra apenas as posições dos elementos, 0, 1, 2, 3, 4
# mostra os elementos contidos nos índices.
#    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# Maneira de fazer 3:
#for pos, comida in enumerate(lanche):
#    print(f'Eu vou comer {comida} na posição {pos}')
#print('COMI PRA CARAMBA!')

# print(len(lanche))

lanche = 'hambúrguer', 'suco', 'pizza', 'pudim', 'batata frita'
# Apenas exibe a Tuplas em ordem alfabética, NÃO ALTERA A TUPLA.
# Para mostrar em ordem o Python transforma momentaneamente em LISTA (colchetes[]).
print(sorted(lanche))
# ['batata frita', 'hambúrguer', 'pizza', 'pudim', 'suco'] # mostra como lista.
print(lanche)
# ('hambúrguer', 'suco', 'pizza', 'pudim', 'batata frita')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
# (2, 5, 4, 5, 8, 1, 2) Apresentam ordem totalmente diferentes.
c = b + a
# (5, 8, 1, 2, 2, 5, 4) Apresentam ordem totalmente diferentes.
print(c)  # Cria uma Tupla 'C' juntando as Tuplas 'A' e 'B'.
# (2, 5, 4, 5, 8, 1, 2)
print(c.count(5))  # Quantas vezes aparece o número 2 na Tupla "c".
# Mostra em que índice está presente o número 8 (a primeira posição em que o número aparece).
print(c.index(8))
print(c.index(2, 4))  # Mostra o índice do número 2 a partir da posição 4.

print(c.index(5, 1))  # Mostra o índice do número 5 a partir da posição 1.

# Em Python podemos misturar números com outros caractéres sem problema (dados de tipos diferente juntos).
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)

# Podemos apagar uma Tupla (toda a Tupla) usando a variável "DEL", nunca podemos apagar elementos em uma Tupla.
del(pessoa)

"""

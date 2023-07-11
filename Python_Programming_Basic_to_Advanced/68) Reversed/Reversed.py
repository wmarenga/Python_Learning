""" 
Reversed:

Obs: Nao confunda com a funcao reverse() que estudamos nas listas.

lista = [1, 2, 3, 4 , 5]
lista.reverse()
print(lista)

tupla = (1, 2, 3, 4 , 5)
tupla.reverse()
print(tupla) # AttributeError: 'tuple' object has no attribute 'reverse'

A funcao reverse() so funciona em listas. Ja a funcao reversed() funciona com qualquer iteravel.

Sua funcao e inverter o iteravel. 

A funcao reversed() retorna um iteravel chamado "list_reverseiterator". 

# Exemplos:

lista = [1,2 ,3 ,4 ,5]
res = reversed(lista)
print(res) # list_reverseiterator object at 0x000002137BC5ADD0
print(type(res)) # class 'list_reverseiterator'

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto. 

# Lista:
print(list(reversed(lista)))

# Tupla:
print(tuple(reversed(lista)))

# Set/ Conjunto:
print(set(reversed(lista))) # O set nao inverte, pois ele nao define ordenacao.
# Obs: Em conjunto, nao definimos a ordem dos elementos.

# Podemos iterar sobre o reversed()
for letra in reversed("Geek University"):
    print(letra, end='') # Imprime tudo na mesma linha.
    
print('\n') # Pular uma linha

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University')))) # Quando usamos o .join(), estamos transformando 
                                                # uma lista de strings em uma string novamente.

# Ja vimos como fazer isso mais facil com o slice de strings
print('Geek University'[::-1])

# Podemos tambem utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n, end=', ')

print('\n') # Pular uma linha

# Apesar que tambem ja vimos como fazer isso utilizando o proprio range()
for n in range(9, -1, -1):
    print(n, end=', ')
"""
for n in range(9, -1, -1):
    print(n, end=', ')
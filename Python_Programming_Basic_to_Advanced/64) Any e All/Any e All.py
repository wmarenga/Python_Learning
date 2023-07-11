""" 
Any e All (Built-in):

all() => Retorna True se todos os elementos do iteravel sao verdadeiros ou ainda se o iteravel 
esta vazio.
Any() => Retorna True se qualquer elemento do iteravel for verdadeiro. Se o iteravel estiver vazio, retorna False.

# Exemplo all():

print(all([0, 1, 2, 3, 4])) 

# Todos os numeros sao verdadeiros? O resultado sera False, pois somente o zero e False.

print(all([1, 2, 3, 4])) # Lista
# O resultado sera True, pois todos os elementos sao verdadeiros.

print(all([])) # Lista vazia
# O resultado sera True, pois todos os elementos sao verdadeiros.

print(all((1, 2, 3, 4))) # Tupla
# O resultado sera True, pois todos os elementos sao verdadeiros.

print(all('Geek')) # String
# O resultado sera True, pois todos os elementos sao verdadeiros.

nomes = ['carlos', 'Camila', 'Carla', 'cassiano' , 'Cristina']
# Se acrescentarmos o nome 'Daniel', mudara para False, pois nem todos os nomes comecam com 'C'.
print(all([nome[0].capitalize() == 'C' for nome in nomes]))

print(all([letra for letra in 'eio' if letra in 'aeiou']))
Obs: Um itaravel vazio convertido em boolean e False, mas o all() entende como True.

print(all(num for num in [4, 2, 10 , 6, 8] if num % 2 == 0))

# Exemplo de Any():

print(any([0, 1, 2 ,3, 4])) # retorna True (basta ter um verdadeiro para ser True)

print(any([0, False, {}, (), []])) # Todos os elementos sao False.

nomes = ['carlos', 'Camila', 'Carla', 'cassiano' , 'Cristina', 'Vanessa']
print(any([nome[0].capitalize() == 'C' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))

"""



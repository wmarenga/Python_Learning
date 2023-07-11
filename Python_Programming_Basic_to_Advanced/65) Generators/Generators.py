""" 
Generators Expression:

Em aulas anteriores nos estudamos: 
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Nao vimos:
- Tuple Comprehension ..... porque se chamam Generators;

nomes = ['Carlos', 'Camila', 'carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0].capitalize() == 'C' for nome in nomes]))

# Poderiamos ter feito utilizando Generators
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes])) # List Comprehension
print(any((nome[0] == 'C' for nome in nomes))) # Generator

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(type(res))

# Generator (Gasta menos recurso no computador - em memoria)
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(type(res))

# Qual e a utilizadade de getsizeof()? Retorna a quantidade de bytes em memoria do 
# elemento passado como parametro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' esta ocupando em memoria. Quanto maior a string,
# mais espaco ocupa.
print(getsizeof('Geek')) # 53 bytes
print(getsizeof('University')) # 59 bytes
print(getsizeof(9)) # 28 bytes
print(getsizeof(91)) # 18 bytes
print(getsizeof(92345668823)) # 32 bytes
print(getsizeof(True)) # 28 bytes

nomes = ['Carlos', 'Camila', 'carla', 'Cassiano', 'Cristina', 'Vanessa']
print(getsizeof([nome[0] == 'C' for nome in nomes])) # 120 bytes
print(type([nome[0] == 'C' for nome in nomes]))
print(getsizeof((nome[0] == 'C' for nome in nomes))) # 104 bytes
print(type((nome[0] == 'C' for nome in nomes)))

from sys import getsizeof

# Gerando uma lista de numeros com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de numeros com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Dictionary Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa, gastamos em memoria: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')

# Eu posso iterar no Generator Expression? SIM

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
"""

"""
# Python grouping data elements (Itertools groupby):

"""
import itertools

# Criar um iterador que retorna keys consecutivas e groups de um iterável
numeros = [100, 90, 70, 50, 50, 100, 100, 80, 90, 80, 83, 83, 20, 20, 20]

keys = list()
groups = list()
numeros_agrupados = sorted(numeros)

for k, g in itertools.groupby(numeros_agrupados):
    # Adicionando os elementos únicos na lista keys (ordenados)
    keys.append(k)
    # adicionando lista de elementos repetidos agrupados na
    # lista groups (ordenandos)
    groups.append(list(g))
print('elementos únicos ordenanos', keys)
print('listas com elementos iguais agrupados e ordenandos', groups)

# Contagem de cada elemento agrupado
contagem_por_grupo = [len(i) for i in groups]
for n in range(0, len(keys)):
    print(f'O número {keys[n]} tem {contagem_por_grupo[n]} elementos.')

# Utilizando zip (dicionário com valores únicos: números agrupados)
valores_zip = dict(zip(keys, contagem_por_grupo))
print(valores_zip)

# Usando comprehensions
letra_misturadas = 'ZZDDFFFUUUooopppkkkkWWWSSSSggggg'
# com todos os valores separados em listas dentro de lista
letras_ordenadas = sorted(letra_misturadas)
print(letras_ordenadas)

# List comprehension (pegando somente os valores únicos => keys)
valores_unicos = [k for k, g in itertools.groupby(letras_ordenadas)]
print('Somente valores únicos', valores_unicos)

# List comprehension (agrupando os valores iguais => groups)
valores_agrupados = [len(list(g))
                     for k, g in itertools.groupby(letras_ordenadas)]
print(valores_agrupados)

for n in range(0, len(valores_unicos)):
    print(
        f'O número {valores_unicos[n]} tem {valores_agrupados[n]} elementos.')

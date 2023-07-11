"""
MAP:

Atencao: Nao confundir este map com o dicionario.
Com map, fazemos mapeamento de valores para funcao.

import math

def area(r):
    "Calcula a area de um  circulo com raio 'r'. "
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))


raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma Comum

areas = []
for r in raios:
    areas.append(area(r))


print(areas)

# Forma com MAP
# MAP e uma funcao que recebe dois parametros: O primeiro
# a funcao, o segundo um iteravel.
# O MAP pega todos os valores na lista raios e passar para a funcao
# area.
# map(funcao - comum ou Lambda, valores).
areas = map(area, raios)

print(areas)
print(type(areas))
print(list(areas)) # Podemos converter para lista, tuplas, etc.

# MAP com Lambda
raios = [2, 5, 7.1, 0.3, 10, 44]
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Obs: Apos utilizar a funcao map() depois da primeira utilizacao do resultado
# (Ex.: conversar para lista e etc), ele zera (limpa a memoria).

# Para fixar (MAP):
# Temos dados iteraveis
# dados: a1, a2, a3, ... , an
# Temos uma funcao:
# Funcao: f(x)
# Utilizamos a funcao map(f, dados), onde map ira 'mapear' cada
# elemento dos dados e aplicar a funcao.

# O MAP object: f(a1), f(a2), f(a3), f(an)

# Mais Exemplo (Converter as temperaturas para Fahrenheit):

import math
cidades = [('Berlim', 29), ('Cairo', 36),('Buenos Aires', 19),
('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]

print(cidades)

# f = 9/5 * c + 32

# Lambda (Arredondando para 2 casas decimais)
conv_cels_fah = lambda dado: (dado[0], round(((9/5) * dado[1] + 32),2))

print(list(map(conv_cels_fah, cidades)))
# Obs: Na funcao 'MAP' somente podemos inserir um parametro para a
# funcao; map(funcao, valores)
"""
# Mais Exemplo (Converter as temperaturas para Fahrenheit):

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19),
           ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]

print(cidades)

# f = 9/5 * c + 32

# Lambda (Arredondando para 2 casas decimais)


def conv_cels_fah(dado): return (dado[0], round(((9/5) * dado[1] + 32), 2))


print(list(map(conv_cels_fah, cidades)))

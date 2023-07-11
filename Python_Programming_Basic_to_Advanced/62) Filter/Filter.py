""" 
Filter:

A funcao Filter serve para filtrar dados de uma determinada colecao. 

# Biblioteca para trabalhar com dados estatisticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1 ]

# Calcular a media aritmetica dos dados utilizando a funcao mean()

media = statistics.mean(dados)
print(media)

# Obs: Assim como a funcao map(), a filter() recebe dois parametros, sendo uma funcao e um iteravel.
# dados => Recebe cada um dos valores na lista dados
# lambda sera a funcao que recebera dados da lista ()
# Sera gerado True ou False em lambda.
res = filter(lambda valor: valor > media, dados)
print(type(res)) # filter object
print(list(res))

# Atencao! Assim como aconteceu na funcao map(), uma vez utilizados os dados de filter(), os mesmo serao eliminado da memoria.
# Outra utilizacao do filter() e a remocao de dados faltantes

# Primeira forma
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

# O None representa os espacos em branco
res = filter(None, paises)

print(list(res))

# Segunda forma (com lambda)
# len(pais) > 0 => todos os paises com mais de uma letra
res = filter(lambda pais: len(pais) > 0, paises)

print(list(res))

# Terceira forma
res = filter(lambda pais: pais != '', paises)

print(list(res))

# A diferenca entre map() e filter() e:

# map(), retorna outros valores (nao somente True ou False) => recebe dois parametros, uma funcao 
# e um iteravel e retorna um objeto mapeando a funcao para cada elemento do iteravel.

# filter(), sempre retorna True ou False => recebe dois parametros, uma funcao e um iteravel e 
# retorna um objeto filtrando apenas os elementos de acordo com a funcao.
# Exemplo mais complexo:

usuarios = [
{'username': 'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizza']},
{'username': 'carla', 'tweets': ['Eu amo meu gato']},
{'username': 'jeff', 'tweets': []},
{'username': 'bob123', 'tweets': []},
{'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'vou sair hoje']},
{'username': 'gal', 'tweets': []},
]

#print(usuarios)

# Tarefa: Filtrar os usuarios que estao inativos no Twitter

# Exemplo professor
inativos = list(filter(lambda user: len(user['tweets']) == 0, usuarios))

# Meu exemplo
#inativos = list(filter(lambda user: user['tweets'] == [], usuarios))
print(inativos)

# Forma 2:
inativos = list(filter(lambda user: not user['tweets'], usuarios))

print(inativos)

# Combinacao de filter() e map()
nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua estrutura e' + nome, desde que cada nome tenha menos 
# de 5 caracteres.

lista = list(map(lambda nome: f'Sua instrutora e {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

# Passo a passo:

# Filtrando os nomes menores que 5
nome_menor = list(filter(lambda nome: len(nome) < 5, nomes))
print(nome_menor)

# Sera criada uma lista com a informacao do filter() que entra na funcao lambda do map().
inf_nome = list(map(lambda nome: f'Sua instrutora e {nome}', nome_menor))
print(inf_nome)

"""
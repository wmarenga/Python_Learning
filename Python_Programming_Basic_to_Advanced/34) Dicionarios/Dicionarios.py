"""
Dicionários:

Obs: Em algumas linguagens de programação, os dicionários Python são conhecidos
por mapas.

Dicionários são coleções do tipo chave/ valor.

# Em dicionários as chaves são explícitas e customizaveis.

Dicionários são representados por chaves {}.
>>> print(type({}))
>>> <class 'dict'>

# A separação entre chave e valor é feita por dois pontos (chave: valor);
# Cada conjunto de chave e valor, representa um elemento;
# Tanto chave quanto valor poderão ser de qualquer tipo de dado, podendo ser misturados.

# Forma 1 (mais comum de criação de dicionário):
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (Menos comum):

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista e tupla pelo colchete [chave].
print(paises['br'])
# print(paises['py'])
# No case de tentármos utilizar chaves inexistentes, será mostrado o erro "KeyError"
# print(paises['ru'])

# Forma 2 - Acessando via "get" (Recomendado)

print(paises.get('br'))
print(paises.get('ru'))  # Não apresenta erro e sim o tipo "None"

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Caso o "get" não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError.

pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print(f'Eu não encontrei o país {pais}')

# Encontrado
pais = paises.get('py')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Eu não encontrei o país')

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Procure o país 'ru' e caso não encontre mostre 'Não encontrado', este seria um valor padrão.
pais = paises.get('py', 'Não encontrado')
print(f'Encontrei o país {pais}')

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print('br' in paises)
print('ru' in paises)  # Não existe esta chave.
print('Estados Unidos' in paises) 

# Nao existe uma chave 'Estados Unidos' e sim um  valor (procura somente pela chave)
# Somente busca pela chave, sendo assim é "False"
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean, lista, tupla, dicionário, como 
chaves de dicionários).

# Tuplas são interessantes serem utilizadas como chaves de dicionários, pois são inalteráveis.
localidades = {(35.6895, 39.6917): 'Escritório em Tókio', (40.7128, 74.0060): 'Escritório em Nova York', 
(37.7749, 122.4194): 'Escritório em São Paulo', }

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Atualizando dados em um dicionario

# Forma 1 (mais comum):
receita['abr'] = 350
print(receita)

# Forma 2:

novo_dado = {'mai': 500}
receita.update(novo_dado)  # Outra forma -> receita.update({'mai': 500})
print(receita)

Meu exemplo (inserindo dados de uma lista para um dicionario):

lista = ['a', 'b', 'c']
dicionario = {}

for i, v in enumerate(lista):
    dicionario.update({i:v})
    
print(dicionario)

# Atualizando dados em um dicionário

# Forma 1:

receita['mai'] = 550
print(receita)

# Forma 2:

receita.update({'mai': 600})
print(receita)

# Conclusão 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# Conclusão 2: Em dicionários NÃO podemos ter chaves repetidas.

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma 1 (mais comum) # Somente pela chave:
# O comando "pop" remove sempre o último elemento de uma lista, porem no dicionario podemos remover de qualquer posicao.
# Remove e retorna o valor removido

ret = receita.pop('jan')
print(ret)
print(receita)

# Obs 1: Aqui precisamos SEMPRE informar a chave, e caso não encontremos o elemento será mostrado um KeyError.
# Obs 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2 (Neste caso o valor removido não será retornado):

del receita['fev']
print(receita)

del receita['fev']  # Se a chave não existir, será gerado um KeyError.

# Porque utilizar dicionários?

Exemplo: Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;

# Opção 1: Poderíamos utilizar uma lista para isso? Sim.

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
print(type(carrinho))

# Teríamos que saber qual é o índice de cada informação no produto 
(índice 0 -> nome, índice 1 -> quantidade, índice 2 -> preço)

# Opção 2: Poderíamos utilizar uma tupla para isso? Sim, qualquer tipo de coleção.

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)
print(type(carrinho))

# Opção 3: Poderíamos utilizar um dicionário para isso? Sim.

carrinho = []

produto1 = {'nome': 'Playstation 4', 'Quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War', 'Quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos e removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação.

>>> dir({})
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
'__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault',
'update', 'values']

# Métodos de dicionários.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# 1- Limpar o dicionário

d.clear()
print(d)

# 2- Copiando um dicionário para outro

# Forma 1 (Deep Copy):

novo = d.copy()
print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 (Shallow Copy):

novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)

# Forma não usual de criação de dicionários:

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

# Os valores entre colchetes serão as chaves e o elemento "desconhecido" será atribuido para cada chave.
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método "fromkeys" recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

# Não acrescentou os últimos 't' e 'e', pois não existe repetição de chave.
veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

"""

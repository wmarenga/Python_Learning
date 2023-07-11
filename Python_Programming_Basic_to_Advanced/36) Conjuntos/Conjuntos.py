"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo uma referência à teoria dos conjuntos da matemática.

No Python, os conjuntos são chamados de "sets".

Dito isto, da mesma forma que na matemática:

- "Sets" (conjuntos) não possuem valores duplicados;
- "Sets" (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos 
com a ordenação deles.
Quando não precisamos se preocupar com chaves, valores e ítens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}, como nos dicionários/ mapas.

Diferença entre conjuntos (sets) e mapas (Dicionários) em Python:
    - Um dicionário tem chave: valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1:

# Repare que temos valores repetidos.
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(s) # Sao exibidos todos os valores unicos (sem repeticoes)
print(type(s))

# Obs: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar error
# e não fará parte do conjunto.

# Forma 2 (mais comum):

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Convertendo Strings para um set
s = set('Geek University')
print(s)

# Convertendo uma Tupla em um set
tupla = (1, 3, 4, 2, 6, 7)
nova = set(tupla) # gera um set com os valores da tupla sem repeticoes

# Podemos verificar se determinado elemento está contido no conjunto.
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem.

# Lista aceitam valores duplicados (10 elementos).
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados (10 elementos).
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34) # ou sem parênteses.
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios Não aceitam chaves duplicados (8 elementos).
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos Não aceitam valores duplicados (8 elementos). 
# Não ordena os elementos e também não mantêm a ordem que definimos.
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python, podemos colocar tipos de dados misturados em "sets".

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente.

for valor in s:
    print(valor)

# Usos interessantes com "sets".

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
informam manulamente a cidade de onde vieram. Nós adicionamos cada cidade em uma lista Python, já 
que em uma lista podemos adicionar novos elementos e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande',
           'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas (unicas) temos na lista.
O que você faria? Faria um loop na lista..?

Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto:
s = {1, 2, 3}
s.add(4)

# Duplicidade de valores não gera Erro, somente ignora a adição do elemento.
s.add(1)
print(s)

# Remover elementos em um conjunto.

# Forma 1:

s.remove(3)  # Nào é índice e sim o valor a ser removido.
# s.remove(33) # Se o valor não for encontrado no conjunto, será gerado o "KeyError". Nenhum valor e retornado
print(s)

s.discard(2)
s.discard(22)  # Se o valor não for encontrado, nenhum erro é gerado.
print(s)

s = {1, 2, 3}
print(s)

# Copiando um conjunto para outro.

# Forma 1 (Deep Copy):

s = {1, 2, 3}
novo = s.copy()  # Criamos uma nova cópia independente do original.
print(novo)

novo.add(4)
print(novo)
print(s)

# Forma 2 (Shallow Copy):

s = {1, 2, 3}
novo = s  # Estabelecemos uma ligação entre as duas variáveis.
novo.add(5)
print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s = {1, 2, 3}
print(s)
s.clear()  # Remove todos os elementos de um conjunto.
print(s)

# Métodos Matemáticos de Conjuntos.

# Imagine que temos 2 conjuntos: 
um contendo estudantes do curso de Python e o outro contendo estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia',
                     'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos.

# Forma 1 (Utilizando union):

# É a união entre os estudantes de Python e Java.
unicos1 = estudantes_python.union(estudantes_java)

# É a união entre os estudantes de Python e Java.
unicos2 = estudantes_java.union(estudantes_python)  # Mesmo resultado.

! Exatamente a mesma ordem em unico1 e unico2.
print(unicos1)
print(unicos2)

# Forma 2 (Utilizando o caractere pipe |):

unicos3 = estudantes_python | estudantes_java
print(unicos3)

# Gerar um conjunto de estudantes que estão em ambos os cursos.

# Forma 1 (Utilizando intersection):

estudantes_python = {'Marcos', 'Patricia',
                     'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 (Utilizando o &):

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudante que não estão no outro curso.

estudantes_python = {'Marcos', 'Patricia',
                     'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

so_python = estudantes_python.difference(estudantes_java) # Somente fazem o curso de Python.
print(so_python)

so_java = estudantes_java.difference(estudantes_python) # Somente fazem o curso de Java.
print(so_java)

# Soma*, Valor Máximo*, Valor Mínimo* , Tamanho.

! * Se os valores forem inteiros ou reais.

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

>>> dir(s)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
'__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__',
'__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__',
'__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__',
'__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__',
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
"""

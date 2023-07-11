"""
Tuplas (tuple):

Tuplas são bastante parecidas com listas.
Existem basicamente duas diferenças básicas:

1) As tuplas são representadas por parênteses ();
# print(type())

2) As tuplas são imutáveis: Isto significa que ao se criar uma tupla, ela permanecerá 
inalterada. Toda operação em uma tupla gera uma nova tupla.

# Atenção 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6,)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6  # Mesmo sem () ele considera tupla.
print(tupla2)
print(type(tupla2))

# Atenção 2: Tuplas com 1 elemento

tupla3 = (4)  # Não é uma tupla (é um número int)!
print(tupla3)
print(type(tupla3))

tupla4 = (4,)  # É uma tupla!
print(tupla4)
print(type(tupla4))

tupla5 = 4, # Não podemos esquecer da vírgula.
print(tupla5)
print(type(tupla5))

# Conclusão: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso do 
parênteses.

(4)  -> Não é uma tupla
(4,) -> É uma tupla
4    -> Não é uma tupla
4,   -> É uma tupla

# Podemos gerar uma tupla dinamicamente com range(início, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla:

tupla = ('Geek University', 'Programação em Python: Essencial')
# As tuplas se comportam como listas (mesmas funcionalidades)
escola, curso = tupla
print(escola)
print(curso)
# Será gerado ERRO se a quantidade de elementos for diferente (deverá ter o número 
exato de elementos).

! Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato 
! das tuplas serem imutáveis.

Soma*, Valor Máximo*, Valor Mínimo* e Tamanho

# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla)) # Somente números inteiros ou reais.
print(max(tupla)) # Somente números inteiros ou reais.
print(min(tupla)) # Somente números inteiros ou reais.
print(len(tupla)) # Pedemos utilizar quaisquer elementos.

# Concatenação de tuplas:

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

# As tuplas podem ser mostradas juntas, porém não serão alteradas (imutáveis).
print(tupla1 + tupla2)
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

# As tuplas são imutáveis mas podemos sobrescrever seus valores.
tupla1 = tupla1 + tupla2  # Redefine os valores de tupla1.
print(tupla1)

# Verificar se determinado elemento está contido na tupla.

tupla = (1, 2, 3)
print(3 in tupla)  # True

print(33 in tupla)  # False

# Iterando sobre uma tupla.

tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla): # Lista os índices e elementos.
    print(indice, valor)

# Contando elementos dentro de uma tupla.

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))  # Conta quantos elementos em uma tupla.

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

# Dicas na utilização de tupla.
# Devemos utilizar tupla SEMPRE que NÃO precisarmos modificar os dados contidos em 
uma coleção.

# Exemplo 1:

# TUPLA
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# LISTA
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Nesta situação não faz sentido inserir valores, sendo assim devemos definir como TUPLA.
meses.append('Playstation')
print(meses)

# Acesso a elementos de uma tupla também é semelhante a de uma lista.

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses[5])  # Mostra o elemento do índice 5.

# Iterar com while.

i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual índice um elemento está na tupla.

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses.index('Junho'))

# Obs: Caso o elemento não exista, será gerado "ValueError".

print(meses.index('Playstation'))

# Se tivérmos 2 elementos iguais, somente será exibido o primeiro (menor índice) 
elemento da tupla.

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Junho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')  
# Será exibido o índice 5.

# Também poderíamos especificar, a partir de qual índice será exibido.

print(meses.index('Junho', 6))  # Sendo assim será exibido o índice 6.

# Slicing
# Tupla[início:fim:passo]

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Junho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses[0:6:2]) 
# Começa no índice 0 e termina no índice 6, avançado 2 índices ('Janeiro, 'Março', 'Maio').

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla não temos o problema de "Shallow Copy".

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra
print(nova)
print(tupla)

dir(tupla) # Temos poucas opções para tuple.
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
 '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
  '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
   '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
    '__subclasshook__', 'count', 'index']

# Por que utilizar tuplas?

1 -> Tuplas são mais rápidas do que listas;
2 -> Tuplas deixam seu código mais seguro*;
* Trabalhar com elementos imutáveis traz segurança para o código.
"""

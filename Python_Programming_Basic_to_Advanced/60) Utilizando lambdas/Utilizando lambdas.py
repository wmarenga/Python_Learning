"""
Utilizando Lambdas:

Conhecidas por expressoes Lambdas, ou simplesmente Lambdas, sao funcoes sem nome,
ou seja, funcoes anonimas. 

# Funcoes em Python

# Funcao normal
def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))

# Exemplo de expressao Lambda (toda expressao comeca com a palavra lambda)
lambda x: 3 * x + 1

# E como utilizar a expressao lambda?
# Para utilizarmos a funcao lambda, devemos atribuir uma variavel a ela (esta maneira nao e a mais usual)
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Podemos ter expressoes lambdas com multiplas entradas

# strip() => remove espacos no inicio e/ ou fim da variavel (somente os espacos externos).
# title() => Converte a primeira letra de um conjunto de strings em maiuscula.

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()


print(nome_completo('Angelina', 'JOLIE'))
print(nome_completo('  FELICITY        ', ' jones     '))

# Em funcoes Python podemos ter nenhuma ou varias entradas. Em Lambdas tambem

amar = lambda: 'Como nao amar Python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1/ y + 1/ z)

# Estrutura da funcao lambda
# n = lambda x1, x2, x3, ..., xn: <expressao>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# Obs: Se passarmos mais argumentos do que parametros esperados, teremos TypeError.

# Outro Exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card','Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

# Ordenando a lista pelo sobrenome
# Funcao Sort()
help([].sort)

Help on built-in function sort:

sort(*, key=None, reverse=False) method of builtins.list instance
    Sort the list in ascending order and return None.
    
    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
    order of two equal elements is maintained).
    
    If a key function is given, apply it once to each list item and sort them,
    ascending or descending, according to their function values.
    
    The reverse flag can be set to sort in descending order.

# Usaremos o parametro key
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
# O resultado sera uma ordenacao pela primeira letra do sobrenome
['Douglas Adams', 'Isaac Asimov', 'Leigh Brackett', 'Ray Bradbury', 'Orson Scott Card', 'Arthur C. Clarke', 'Robert Heinlein', 'Frank Herbert', 'H. G. Wells']

# O split separa a sequencia de strings pelos espacos
# [-1] => pega o ultimo caractere
# lower() => transforma tudo em minusculo para todos fiquem iguais
nome = 'Orson Scott Card'
nome.split(' ')[-1].lower()
print(nome)

# Funcao quadradica

# f(x) = a * x ** 2 + b * x + c (ax2 + bx + c)

# Definindo a funcao

def geradora_funcao_quadradica(a, b, c):
    "Retorna a funcao f(x) = a * x ** 2 + b * x + c"
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadradica(2, 3, -5) # Valore de a, b, c (serao inseridos argumentos para a funcao comum)

print(teste(0)) # Valor de x para a funcao lambda
print(teste(1)) # Valor de x para a funcao lambda
print(teste(2)) # Valor de x para a funcao lambda

# Poderiamos inserir os argumentos direto no print (a, b, c)(x)
print(geradora_funcao_quadradica(2, 3, -5)(0))
print(geradora_funcao_quadradica(2, 3, -5)(1))
print(geradora_funcao_quadradica(2, 3, -5)(2))

# Geralmente utilizamos a funcao lambda para fazer filtragem ou ordenacao de dados

"""

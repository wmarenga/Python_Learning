"""
Documentacao Python:

https://docs.python.org/release/3.10.4/library/exceptions.html

Erros mais Comuns em Python:

printf('Geek University')

Saida:

File "d:\23) Programacao\Cursos\Python\9) Programacao em Python do Basico ao avancado - 65,5 horas\73) 
Erros mais Comuns em Python\Erros mais Comuns em Python.py", line 6, in <module>
    printf('Geek University')
NameError: name 'printf' is not defined. Did you mean: 'print'?

ATENCAO! E importante prestar atencao e aprender a ler as saidas de erros geradas oeka execucao do 
nosso codigo.

*****************************************************************************************************
Os erros mais comuns:

SyntaxError => Ocorre quando quando uma variavel ou funcao nao foi definida.

NameError => Ocorre quando o Python encontra um erro de sintaxe. Ou seja, voce escreveu algo que
o Python nao reconhece como parte da linguagem.

TypeError => Ocorre quando uma funcao/ operacao/ acao e aplicada a um tipo errado.

IndexError => Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado, 
utilizando um indice invalido.

ValueError => Ocorre quando uma funcao/ operacao built-in (integrada), recebe uma argumento com tipo
correto mas valor inapropriado.

KeyError => Ocorre quando tentamos acessar um dicionario com uma chave que nao existe.

AttributeError => Ocorre quando uma variavel nao tem um atributo/ funcao.

IndentationError => Ocorre quando nao respeitamos a indentacao do Python (4 espacos).

*******************************************************************************************************

# 1 - Exemplos SyntaxError:

a) Temps que usar parenteses para definir uma funcao

def funcao: # Faltam os parenteses
    print('Geek University') # SyntaxError: invalid syntax
b) Nao podemos utilizar palavras reservadas como nomes de variaveis

None = 1 # SyntaxError: cannot assign to None
def = 1 # SyntaxError: cannot assign to def

# c) O return tem que utilizado dentro de uma funcao

return => # SyntaxError: 'return' outside function

# 2 - Exemplos NameError:

# Exemplos de NameError

#print(geek) # NameError: name 'geek' is not defined
#geek() # NameError: name 'geek' is not defined

# Este erro ocorre bastante quando estamos trabalhando com variaveis locais e globais
a = 18
if a < 10:
    msg = 'E maior que 10'
    

print(msg) # NameError: name 'msg' is not defined (pois a variavel msg so vai existir quando a < 10).

# 3 - Exemplos de TypeError:

# Exemplos de TypeError:

print(len(5)) # TypeError: object of type 'int' has no len()
print('Geek' + []) # TypeError: can only concatenate str (not "list") to str
print('Geek' + 4) # TypeError: can only concatenate str (not "int") to str
print('Geek' + str(4)) # Convertendo tudo para o mesmo tipo, conseguimos fazer a soma

# 4 - IndexError:

# Exemplos de IndexError:

lista = ['Geek'] # Poderia ser qualquer elemento indexado (tupla, set, dicionario)
print(lista[2]) # IndexError: list index out of range
print(lista[0][10]) # IndexError: list index out of range (nao existe a posicao 10)

# 5 - ValueError:

# Exemplos de ValueError:

print(int('Geek')) # ValueError: invalid literal for int() with base 10: 'Geek'
print(float('Geek')) # ValueError: could not convert string to float: 'Geek'
# 6 - KeyError

# Exemplos de KeyError

dic = {}
print(dic['geek']) # KeyError: 'Geek'

dic2 = {'Python': 'University'}
print(dic2['geek']) # KeyError: 'geek'

# 7 - AttributeError:

# Exemplos de AttributeError:

tupla = (11, 2, 31, 4) # Tuplas sao imutaveis
tupla.sort() # AttributeError: 'tuple' object has no attribute 'sort'
print(tupla)

# 8 - IndentationError:

# Exemplos de IndentationError:

def nova():
print('Geek') # IndentationError: expected an indented block after function definition on line 116

nova()

for i in range(10):
i + 1 # IndentationError: expected an indented block after 'for' statement on line 121


print(i)

Obs1: Exceptions e Erros sao sinonimos na programacao.
Obs2: Importante ler e prestar atencao na saida de erro.
"""

""" 
Reduce:
Obs: A partir do Python3+ a funcao reduce() nao e mais uma funcao integrada (built-in).
Agora temos que importa para utilizar esta funcao a partir do modulo 'functools'.

Guido Van Rossum (Criado do Python): Utilize a funcao reduce() se voce realmente precisa
dela. Em todo caso 99% das vezes um loop For e mais legivel.

Para entender o reduce():

# Imagine que voce tem uma colecao de dados:

dados = [a1, a2, a3, ..., an]

# E voce tem uma funcao que recebe dois parametros:

def funcao(x, y):
    return x, y
    

Assim como map() e filter(), a funcao reduce() recebe dois parametros: a funcao e o iteravel.
reduce(funcao, dados)

A funcao reduce(), funcionara da seguinte forma:
    passo 1: res1 = f(a1, a2) # Aplica a funcao nos dois primeiros elementos da colecao e guarda o resultado.
    passo 2: res2 = f(res1, a3) # Aplica a funcao passada, o resultado do passo 1, mais o terceiro elemento e guarda o res.

    Isso e repetido ate o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    passo n: resn = f(resm, an)

ou seja, em cada passo ela aplica a funcao passado como primeiro argumento, o resultado da aplicacao anterior. 
No final, reduce() ira retornar o resultado final.

Alternativamente, poderiamos ver a funcao reduce() como:
funcao(funcao(funcao(funcao(funcao(a1, a2), a3), a4), ...), an)

# Como funciona na pratica?

# Vamos utilizar a funcao reduce() para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nos precisamos de uma funcao que receba dois parametros
multi = lambda x, y: x * y

res = reduce (multi, dados)
print(res)
# Fara a multiplicacao sucessiva do resultado anterior com o numero atual (analizado).

# Agora utilizaremos um loop nomal (for)
res = 1
for n in dados:
    res = res * n

print(res)

"""

'''
Numeros:

Símbolo     Descrição
  (+)         soma
  (-)       subtração
  (*)     multiplicação
  (/)        divisão
  (//)  parte inteira da divisão
  (**)      exponencial
   +=    incremento de variáveis
   *=    multiplica incremental de variáveis
   
Referencia Bibliografica:

LEE, Kent D. Python Programming Fundamentals. Second Edition. Springer - Verlag London 2014.
https://link.springer.com/chapter/10.1007%2F978-1-4471-6642-9_8
https://link.springer.com/chapter/10.1007%2F978-1-4471-6642-9_9

a = 5
b = a + a 
print(b)

print(type(b))

a = 5
b = a + 5.
print(b)

print(type(b))

c = 10
c = c + 5
print(c)

c += 5
print(c)

c *= 5
print(c)

c -= 5
print(c)

d = 5**2
print(d)

e = 5
f = 2

Divisao comum
g = e / f
print(type(g))

Divisao com a parte inteira
g = e // f
print(type(g))

Numero Complexo (a parte imaginaria e j e nao i):

g = 5 + 5j
print(type(g))

h = g + g
print(h)

Se quisermos 1j precisamos deixar explicito no numero Complexo
g = 5 +1j

g = 1j 
h = g ** 2
print(g)

O numero imaginario ao quadrado e igual a -1
saida: -1 + 0j
'''
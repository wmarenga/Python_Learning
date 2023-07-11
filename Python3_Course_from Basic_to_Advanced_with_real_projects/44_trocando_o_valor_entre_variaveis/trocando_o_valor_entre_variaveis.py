# Invertendo valores de variáveis
from tkinter import W


x = 10
y = 'Luiz'

# Em outras linguagens
z = x
x = y
y = z
print(f'x = {x} e y = {y}')

# Em Python é muito mais simples

a = 20
b = "Wellington"
a, b = b, a
print(f'a = {a} e b = {b}')

# Embaralhando 3 variáveis

w = 10
q = "Renata"
k = "Marenga"
w, q, k = k, w, q
print(f'w = {w}, q = {q}, k = {k}')

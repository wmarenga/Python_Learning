# Inverting variable values

x = 10
y = 'Luiz'

# In other languages
z = x
x = y
y = z
print(f'x = {x} e y = {y}')

# In Python it is much simpler

a = 20
b = "Wellington"
a, b = b, a
print(f'a = {a} e b = {b}')

# Shuffling 3 variables

w = 10
q = "Renata"
k = "Marenga"
w, q, k = k, w, q
print(f'w = {w}, q = {q}, k = {k}')

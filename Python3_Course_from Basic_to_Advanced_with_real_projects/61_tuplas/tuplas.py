"""
Tuplas:

As tuplas ao contrário das lista, são imutáveis.

#     0  1  2   3         4
t1 = (1, 2, 3, 'a', 'Luiz Otávio')
print(t1)
print(type(t1))

# Acessamos as tuplas pelos índices

print(t1[4])

# Para iterar sobre uma tupla:

for v in t1:
    print(v)

# Fatiamento de tuplas:

print(t1[1:3])

# Podemos criar tuplas sem utilizar os parênteses

t2 = 'w', 'l', 're', 'ru'
print(t2)
t3 = 1,  # temos que adicionar uma vírgula no final para declarar que é tupla
print(t3)
print(type(t3))

# Concatenando tuplas:

ta = 1, 2, 3, 4, 5
tb = 6, 7, 8, 9, 10

tf = ta + tb
print(tf)

# Desempacotando tuplas:

ta = 1, 2, 'Luiz', 4, 5
tb = 6, 7, 8, 9, 10
tf = ta + tb

n1, n2, n3, *_ = tf
nova_tupla = n1, *_  # Criando uma nova tuplas desempacotando
print(n3)
print(nova_tupla)

n1, n2, n3, *_, n10 = tf  # O n10 é o último elemento da tupla
print(n10)

# Exibindo uma tupla multiplas vezes

ta = (1, 2, 'Luiz', 4, 5) * 20
print(ta)

"""
# Convertendo tuplas em listas
tx = 1, 2, 3, 4, 5,
# tx[1] = 3  # TypeError: 'tuple' object does not support item assignment


tx = list(tx)  # Fazendo um cast para transformar tupla em lista
print(tx)
print(type(tx))
print(tx)

tx[1] = 3000  # Após converter para lista, conseguimos alterar.
print(tx)

tx = tuple(tx)  # Fazendo um cast para converter para tupla novamente

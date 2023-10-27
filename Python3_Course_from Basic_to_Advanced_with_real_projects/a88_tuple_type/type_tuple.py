"""
Tuple type - An immutable list

Note: Tuples are faster than lists.

# TypeError: 'tuple' object does not support item assignment
names[1] = 'Another thing'

"""
names = ('Maria', 'Helena', 'Luiz')
# names = 'Maria', 'Helena', 'Luiz'
# names = tuple(names)
# names = list(names)

print(names[-1])
print(type(names))
print(names)

#     0  1  2   3         4
t1 = (1, 2, 3, 'a', 'Luiz Otávio')
print(t1)
print(type(t1))

#! We access tuples through indexes:

print(t1[4])

#! To iterate over a tuple:

for v in t1:
    print(v)

#! Tuple slicing:

print(t1[1:3])

#! We can create tuples without using parentheses:

t2 = 'w', 'l', 're', 'ru'
print(t2)
t3 = 1,  # we have to add a comma at the end to declare that it is a tuple
print(t3)
print(type(t3))

#! Concatenating tuples:

ta = 1, 2, 3, 4, 5
tb = 6, 7, 8, 9, 10

tf = ta + tb
print(tf)

#! Desempacotando tuplas:

ta = 1, 2, 'Luiz', 4, 5
tb = 6, 7, 8, 9, 10
tf = ta + tb

n1, n2, n3, *_ = tf
new_tuple = n1, *_  # Creating a new tuple by unpacking
print(n3)
print(new_tuple)

n1, n2, n3, *_, n10 = tf  # the n10 is the last element of the tuple
print(n10)

#! Displaying a tuple multiple times:

ta = (1, 2, 'Luiz', 4, 5) * 20
print(ta)


#! Converting tuples to lists:
tx = 1, 2, 3, 4, 5,
# tx[1] = 3  # TypeError: 'tuple' object does not support item assignment


tx = list(tx)  # Making a cast to transform a tuple into a list.
print(tx)
print(type(tx))
print(tx)

tx[1] = 3000  # After converting to list, we were able to change.
print(tx)

tx = tuple(tx)  # Making a Casting to convert to tuple again.

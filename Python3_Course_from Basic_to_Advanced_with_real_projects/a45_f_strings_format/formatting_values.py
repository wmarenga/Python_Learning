"""
Formatting values with modifiers:

:s - Text (str);

*Examplo:
name = 'Luiz Otávio'
print(f'{name:s}')

:d - Integers (int);

*Examplo:
age = 51
print(f'{age:d}')

:f - Floating point numbers (float);

*Examplo:
salary = 1200.34
print(f'{salary:f}')

:. (number)f - Quantity of decimal places (float);

*Examplos:
num_1 = 10
num_2 = 3
division = num_1 / num_2
print(division)

# Using .format()
print('{:.2f}'.format(division))

# Using with f-strings
print(f'{division:.2f}')

: (CHARACTER)(> or < or ^)(QUANTITY)(TYPE - s, d or f).

*Examplo:
num_1 = 1
print(f'{num_1:0>10}')  # It will be added 9 zeros.

num_2 = 1150
print(f'{num_2:0>10}')  # It will be added 6 zeros, because we already have 4 numbers.

num_3 = 9999
print(f'{num_3:0^11}')  #It will be added 3 zeros to the left and 4 to the right.

> - Left
< - Right
^ - Center

# Combined

*Exemplo:
num_4 = 1150
print(f'{num_4:0>10.2f}')

# We can use it with str too.

name = 'Otávio Miranda'
print(len(name))
print(50 - len(name))  # Leave my str with 50 characters.

print(f'{name:#^50}')

name_formatado = '{:@>50}'.format(name)

# It doesn't add anything, as it is already the number of characters in the str.
formatted_name2 = '{:@>14}'.format(name)
print(formatted_name)
print(formatted_name2)

# Named
formatted_name3 = '{n:0<20}'.format(n=name)
print(formatted_name3)

# Using indexes in a str.
name = 'Wellington'
surname = 'Marenga'
formatted_name5 = '{0:-^50}\n''{1:+^50}'.format(name, surname)
#formatted_name6 = '{1:+^50}'.format(name, surname)
print(formatted_name5)
# rint(formatted_name6)

# Using str functions

# Justify to the left
name = 'welLiNgton'
# name = name.ljust(20, '#')
print(name)

# Justifies to the right
name2 = 'Marenga'
name2 = name2.rjust(20, '*')
print(name2)

# Justify to the center
name3 = 'Junior'
name3 = name3.center(20, '@')
print(name3)

print(name.lower())  # all lowercase letters
print(name.upper())  # all uppercase letters
print(name.title())  # only the first letters capitalized
"""

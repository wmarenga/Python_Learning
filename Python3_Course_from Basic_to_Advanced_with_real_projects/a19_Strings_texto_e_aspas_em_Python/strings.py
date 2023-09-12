"""
DocString

Python = Programming language
Type of typing = Dynamic / Strong

str -> string -> text

Strings are texts enclosed in quotation marks (single and double).

print(1234)

# Single quotes
print('Luiz Otávio')
print(1, 'Luiz "Otávio"')

# Double quotes
print("Luiz Otávio")
print(2, "Luiz 'Otávio'")

# Escape
print("Luiz \"Otávio\"")

# r
print(r"Luiz \"Otávio\"")

print('Something')
print("Something")

Python is a dynamically typed language, therefore,the interpreter
will assign a data type according to the informed or assigned parameter.

name = 'Wellington'  # (str)
number_caractere = '123456'  # (str)
number = 123456  # (int)
decimal = 12.11  # (float)
decision = True  # (bool)
list_of_elements = []  # (list)

To check the type, we use the command:
print(type(list_of_elements))
print(type(number))
print(type(12.11))

Quotes within Quotes:

print('This is a "string" (str).')
print("This is a 'string' (str).")

Using escape characters (only used as a last resort):

print('This is a \'string\' (str).')
print("This is a \"string\" (str).")

Line break:

print("This is a \nstring (str).")

Using the raw strings:

print(r'This is a \nstring (str).')

Obs: It cannot be used to ignore equal internal quotes (single or double).

# Does not work
print(r'This is a 'string' (str).')
print(r"This is a "string" (str).")

Error displayed:
SyntaxError: invalid syntax. Perhaps you forgot a comma?
"""

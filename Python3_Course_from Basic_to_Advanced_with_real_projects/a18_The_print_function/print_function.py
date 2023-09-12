"""
\r\n -> CRLF (Windows)
\n -> LF (Linux)
print(12, 34, 1011, sep="", end='\r\n')
print(12, 34, 1011, sep="", end='#')
print(12, 34, 1011, sep="", end='##\n')
print(12, 34, 1011, sep="", end='\n##')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')

The print is an internal Python function. Its functionality
is to show the information passed in parentheses or by (f-strings).

Example in parentheses:
print(123456)
print('Hi')
# By default, will be added a space after each comma.
print('Luiz', 'Otávio', 'Another thing')

# If we perform a sum operation, we will not have the
spaces, as the parameters are being concatenated.
print('Luiz'+'Otávio'+'Another thing')

# Print with named argument (sep=) - Separator:

In the same line:
print('Luiz', 'Otávio', sep='-')
print('João', 'and', 'Maria', sep='-')

Skipping lines
print('Luiz', 'Otávio', sep='-', end=' => ')
print('João', 'and', 'Maria', sep='-', end='')

print('I am', 'learning', 'Python', sep='-', end=' ')
print('this is really', 'cool', sep='-', end='')

Obs: Python differentiates between lowercase and uppercase
letters, so the Print() function does not exist.

Example with f-strings
name = 'Wellington'
print(f'Hello, I am {name}')

CPF Exercise:

Format the CPF number (824.176.070-18) with print().

print('824', '176', '070', sep='.', end='-')
print('18')

With f-string:
cpf_numbers = '82417607018'
print(f'{cpf_numbers[0:3]}.{cpf_numbers[3:6]}.{cpf_numbers[6:9]}-{cpf_numbers[9:11]}')
"""

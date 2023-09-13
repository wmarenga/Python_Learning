"""
Data input:

It will always return a str:

Example:

from datetime import datetime

name = input("What is your name? ")
print(f'The user entered {name} and the variable type is {type(name)}.\n')

# On this way appears, name = entered name.
print(f'Your name is {name = }')

age = input("What is your age? ")
print(f'{name} has {age} years old.')

# Perform age conversion with Type Cast (casting):
birth_year = datetime.now().year - int(age)
print(f'You were born in {birth_year}.')

# Example of a calculator to do sum only:

number_1 = int(input('Enter a number: '))
number_2 = int(input('Enter another number: '))

# The best way is to convert after the user enters the data, as the developer
will be able to know what was entered before the conversion.

int_number_1 = int(number_1)
int_number_2 = int(number_2)

Another option:
number_2 = int(number_2)

print(number_1 + number_2)

Obs: If we convert the sum of the characters, we would be getting
the concatenation result converted to an integer.

print(int(number_1 + number_2))
"""

"""
Variables:

Variables are used to save something in the computer's memory.

PEP8: start variables with lowercase letters, you can use numbers and
underscore _.

The = sign is the assignment operator. It is used to assign a value
to a name (variable).

Using: variable_name = expression

Recommendations:

- Start with letter;
- It may contain numbers, but never start with a number;
- separate by underscore (_);
- Use lowercase letters.

Obs: Every variable allocates space in the computer's memory.

Example:

full_name = 'Luiz Otávio Miranda'
sum_of_2_numbers = 2 + 2
int_one = bool('1')
print(int_one, type(int_one))
print(full_name, sum_of_2_numbers)

name = 'Luiz'
print(name)
print(type(name))

age = 32
height = 1.80
is_legal_age = age > 18
weight = 80
# IMC = weight / (height * height)
imc = weight / (height ** 2)

print('Name: ', name)
print('Age', age)
print('Height', height)
print('Is_legal_age:', is_legal_age)

print(age * height)

# Exercise:
# Calculation of a person's BMI.

weight = 80
height = 1.80
imc = weight / (height ** 2)
print(f'The {name} have {age} years old and your IMC is {imc:.2f}.')
"""

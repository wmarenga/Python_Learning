"""
while in Python:

Used to perform actions while a condition is true.

Requirements: Understand conditions and operators.

# Infinite loop (when a code has no end)

* Example:

while True:
    name = input('What is your name? ')
    print(f'Hello {name}!')

print('It will not be executed.')

# Show a number up to 100
x = 0
while x <= 100:
    print(x, end='-')
    x += 1

print('It's over!')

# Using 'continue'
# It will continue running and skip the x == 3
x = 0
while x < 10:
    if x == 3:
        x += 1
        continue

    print(x)
    x += 1

print('It's over!')

# Using 'break'
# It will stop when x == 3
x = 0
while x < 10:
    if x == 3:
        x += 1
        break

    print(x)
    x += 1

print('It's over!')
x = 0  # Column
while x < 10:
    y = 0  # Line
    while y < 5:
        print(f'({x}, {y})', end=',')
        y += 1
    x += 1  # x = x + 1

print('It's over!')

* Example:

condition = True

while condition:
    name = input('What is your name: ')
    print(f'Your name is {name}')

    if name == 'exit':
        break

print('It's over!')

"""
# Creating a basic calculator
while True:
    print()

    num_1 = input('Type one number: ')
    num_2 = input('Type another number: ')
    operator = input('Type one operator: ')

    if num_1.isalpha() or num_2.isalpha():
        print('Enter an integer value:')
        continue

    elif num_1.isdigit() and num_2.isdigit():
        num_1 = int(num_1)
        num_2 = int(num_2)

    # + - / *
    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1 - num_2)
    elif operator == '/':
        print(num_1 - num_2)
    elif operator == '*':
        print(num_1 * num_2)

    leave = input('Do you want to leave? [y]es or [n]o: ').lower()

    if leave == 'y':
        break

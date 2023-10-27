numbers = [1, 2, 3, 4, 5]
new_numbers = [number for number in numbers]
print(numbers)
print(new_numbers)

#! Creating a new list by dividing by 2:
division = [number / 2 for number in numbers]
print(numbers)
print(division)

#! Creating a new list multiplication by 2
multiplication = [number * 2 for number in numbers]
print(numbers)
print(multiplication)

#! We can also assign functions so that we can use them throughout the code:


def division(x, y):
    return x / y


def multiplication(x, y):
    return x * y


def potentiation(x, y):
    return x ** y


numbers = [1, 2, 3, 4, 5]
division_list = [division(number, 2) for number in numbers]

multiplication_list = [multiplication(number, 2) for number in numbers]

potentiation_list = [potentiation(number, 2) for number in numbers]

print(numbers)
print(division_list)
print(multiplication_list)
print(potentiation_list)

#! Filtering values with list comprehension (conditionals):

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = [number for number in numbers if number > 5]
odd_numbers = [number for number in numbers if number % 2 != 0]
even_numbers = [number for number in numbers if number % 2 == 0]
other_if = [number if number !=
            6 else 600 for number in even_numbers]

print(numbers)
print(new_numbers)
print(odd_numbers)
print(even_numbers)
print(other_if)

#! Using nesting with list comprehension:

combinations = []
for x in range(3):  # 3 lines
    for y in range(2):  # 2 columns
        combinations.append((x, y))
print(combinations)

#! With list comprehension:
combinations = [(x, y) for x in range(3) for y in range(2)]
print(combinations)

#! If we want to skip values:
combinations = [(x, y) for x in range(3) for y in range(3) if x != 2]
print(combinations)

#! If the y is different of 2, display it, otherwise multiply by 1000:
combinations = [(x, y) if y != 2 else (x, y * 1000) for x in range(3)
                for y in range(3) if x != 2]
print(combinations)

#! Manipulating strings:
string = 'Wellington Marenga'
new_string = [letter for letter in string]
print(new_string)

#! Joining again and string:
string = 'Wellington Marenga'
new_string = ''.join([letter for letter in string])
print(new_string)

#! Getting groups of letters jumping 2 by 2:
string = 'Wellington Marenga'
number_of_letters = 3
new_string = [string[index:index + number_of_letters]
              for index in range(0, len(string), 2)]

#! If we want to separate with a dot:
new_string = '.'.join([string[index:index + number_of_letters]
                       for index in range(0, len(string), 2)])
print(new_string)

#! Working with strings inside lists:
names = ['Luiz', 'Maria', 'Helena', 'Joana', 'Felipe']
new_names = [names for names in names]
print(new_names)

#! Leave it lowercase:
new_names_lower = [names.lower() for names in names]
print(new_names_lower)

#! First capital letters:
new_names_upper = [names.title() for names in names]
print(new_names_upper)

#! All capital letters:
new_names_all_upper = [names.upper() for names in names]
print(new_names_all_upper)

#! Leaving the last letter capitalized:
last_upper = [f'{names[:-1].lower()}{names[-1].upper()}' for names in names]
print(last_upper)

#! A single list within a list:
numbers = [[number, number ** 2] for number in range(10)]
flat = [y for x in numbers for y in x]
print(numbers)
print(flat)

"""
For in (Python):
Iterating strings with "for"
Function range(start=0, stop, step=1)

* Example with while:
text = 'Python'

c = 0
while c < len(text):
    print(text[c])
    c += 1

* Example com for:

text = 'Python'

for letter in text:
    print(letter)

* Exemplo with range: range(start=0, stop, step=1):

for n in range(10):
    print(n)
! Output: 0 1 2 3 4 5 6 7 8 9

# Crescent

for n in range(0, 10, 2):
    print(n)

# descending
for n in range(20, 10, -2):
    print(n)

# Using condition:
for n in range(100):
    if n % 8 == 0:
        print(n)

"""
# Using "for" to change letter to uppercase.

# text = 'Python'
# new_string = ''

# for letter in text:
#     if letter == 't':
#         new_string = new_string + letter.upper()
#     elif letter == 'h':
#         new_string += letter.upper()
#     else:
#         new_string += letter

# print(new_string)

# continue => skip to the next loop
# break => finish the loop

# We would not include the letter 't' because the loop will skip the if.
# text = 'Python'
# new_string = ''

# for letter in text:
#     if letter == 't':
#         continue
#         new_string = new_string + letter.upper()
#     elif letter == 'h':
#         new_string += letter.upper()
#     else:
#         new_string += letter

# print(new_string)

# It will stop after including the capital letter 'H'.
# text = 'Python'
# new_string = ''

# for letter in text:
#     if letter == 't':
#         new_string = new_string + letter.upper()
#     elif letter == 'h':
#         new_string += letter.upper()
#         break
#     else:
#         new_string += letter

# print(new_string)

# *Another example (while):

# saved_password = '123456'
# entered_password = ''
# repetitions = 0

# while saved_password != entered_password:
#     entered_password = input(f'You tried ({repetitions} times): ')

#     repetitions += 1

# print(f"You entered the correct password in your {repetitions} attempt.")
# print('That loop above can have infinite repetitions')

# *Another example (for):

# text = 'Python'

# new_text = ''
# for letter in text:
#     new_text += f'*{letter}'
#     print(letter)
# print(new_text + '*')

# prime_number

prime_number = list()
for number in range(1000):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            prime_number .append(number)
    elif number == 0:
        continue
    elif number == 1:
        continue
    else:
        print(number, "it's negative number")

print(prime_number)

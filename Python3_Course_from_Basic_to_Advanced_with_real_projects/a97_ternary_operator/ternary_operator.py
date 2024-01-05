"""
Ternary operator in Python:

Ternary operation (one-line conditional)
<value> if <condition> else <another value>

# condition = 10 == 11
# variable = 'Value' if condition else 'another value'
# print(variable)
# digit = 9  # > 9 = 0
# new_digit = digit if digit <= 9 else 0
# new_digit = 0 if digit > 9 else digit
# print(new_digit)
print('Value' if False else 'another value' if False else 'End')

# *Example of ternary operator:
logged_user = True  # logged
# logged_user = False  # not logged

msg = 'User Logged' if logged_user else 'User needs to log in'

# No ternary
# if logged_user:
#     msg = 'User Logged'
# else:
#     msg = 'User needs to log in'

print(msg)

# * Another example
# No ternary
age = 18

if age >= 18:
    print('You can access.')
else:
    print('You can NOT access.')

"""

# * Another example
# No ternary
age = input("How old are you? ")

while not age.isnumeric():
    print('You only need to enter numbers!')
    age = input('How old are you? ')
else:
    age = int(age)
    is_legal_age = (age >= 18)
    msg = 'You can access.' if is_legal_age else 'You can NOT access.'

print(msg)

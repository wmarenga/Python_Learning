"""
Write a program that asks the user to enter an integer number, informs
whether this number is even or odd. If the user does not enter
an integer number, inform them that it is not an integer number.
"""
number = input('Enter a number: ')

# if number.isdigit():
#     number_int = int(number)
#     even_odd = number_int % 2 == 0
#     even_odd_text = 'odd'

#     if even_odd:
#         even_odd_text = 'even'

#     print(f'The number {number_int} is {even_odd_text}')
# else:
#     print('You did not enter an integer number.')

try:
    number_int = int(number)
    even_odd = number_int % 2 == 0
    even_odd_texto = 'odd'

    if even_odd:
        even_odd_texto = 'even'

    print(f'The number {number_int} is {even_odd_texto}')
except:
    print('You did not enter an integer number.')
"""
Write a program that asks to the user the time and, based on the
time described, displays the appropriate greeting.
Ex. Good morning 0-11, Good afternoon 12-17 and Good evening 18-23.
"""
# time = input('Enter a time (0-23): ')
#
# if time.isdigit():
#     time = int(time)
#
#     if time < 0 or time > 23:
#         print("The time must be between 0 e 23")
#     else:
#         if time <= 11:
#             print('Good morning!')
#         elif time <= 17:
#             print('Good evening!')
#         else:
#             print('Good night!')
# else:
#     print("Please, enter a time between 0 e 23.")
"""
Write a program that asks for the user's first name. If the name has
4 letters or less write "Your name is short"; if it has between 5 and
6 letters, write "Your name is normal"; greater than 6 write "Your
name is too long".
"""
# name = input('Informe your name: ')
# name_size = len(name)
#
# if name_size <= 4:
#     print('Your name is short.')
# elif name_size <= 6:
#     print('Your name is normal.')
# else:
#     print('Your name is too big.')

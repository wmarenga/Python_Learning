"""
Exercise 1:
Write a program that asks the user to enter an integer number, informs
whether this number is even or odd. If the user does not enter
an integer number, inform them that it is not an integer number.
"""
# num = input('Type one number: ')

# while True:
#     if num.isdigit():
#         num = int(num)
#         if num % 2 == 0:
#             print(f'The number {num} is even.')
#         else:
#             print(f'The number {num} is odd.')
#         break
#     elif num.isalpha():
#         print('Enter an integer value!')
#         num = input('Type one number: ')
#     else:
#         print('Enter a valid integer value!')
#         num = input('Type one number: ')

"""
Exercise 2:
Write a program that asks to the user the time and, based on the
time described, displays the appropriate greeting.
Ex. Good morning 0-11, Good afternoon 12-17 and Good evening 18-23.
"""
while True:
    time = input('What time is it now, please? (numbers only): ')
    minute = input('What minute is it now, please? (numbers only): ')
    if time.isalpha() or minute.isalpha():
        print('Enter numbers only!')
        continue
    else:
        time = int(time)
        minute = int(minute)
        if time >= 00 and time < 12:
            print(f'Good morning! Now is {time}:{minute}')
        elif time >= 12 and time < 18:
            print(f'Good afternoon! Now is {time}:{minute}')
        else:
            print(f'Good evening! Now is {time}:{minute}')
    break

"""
Exercise 3:
Write a program that asks for the user's first name. If the name has
4 letters or less write "Your name is short"; if it has between 5 and
6 letters, write "Your name is normal"; greater than 6 write "Your
name is too long".
"""

# first_name = input('Inform your first name: ').capitalize()

# if len(first_name) <= 4:
#     print(
#         f'Hi {first_name}!, your name has only {len(first_name)} letters, your name is SHORT!')
# elif len(first_name) >= 5 and len(first_name) <= 6:
#     print(
#         f'Hi {first_name}!, your name has {len(first_name)} letters, your name is NORMAL!')
# else:
#     print(
#         f'Hi {first_name}!, your name has {len(first_name)} letters, your name is TOO BIG!')

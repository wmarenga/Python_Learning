"""
Introduction to try/except
try -> try to execute the code
except -> an error occurred when trying to execute
"""
number_str = input('I will double the number you enter: ')

try:
    number_float = float(number_str)
    print('Float number:', number_float)
    print(f'The double of {number_str} is {number_float * 2:.2f}')
except:
    print('This is not a number.')

# if number_str.isdigit():
#     number_float = float(number_str)
#     print(f'The double of {number_str} é {number_float * 2:.2f}')
# else:
#     print('This is not a number.')

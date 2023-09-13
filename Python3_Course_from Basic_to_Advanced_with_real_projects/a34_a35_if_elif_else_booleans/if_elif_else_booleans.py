"""
IF, ELIF and ELSE conditions:

if
elif (else if)
else

# Example of if:

if True:
    print('True.')
    num_1 = 2
    num_2 = 4
    print(num_1 + num_2)

if False:
    print('False.')

This expression will be executed even without the if.
print('My expression is not true.').

# Example if, else:

if True:
    print('True')
else:
    print('Not True.')

# Example if, elif, else:

if False:
    print('True.')
elif False:
    print('Now is True.')
    name = input("What is your name? ")
    print(f'Your name is {name}.')
elif True:
    print('More one True.')
    print(22 + 22)
else:
    print('Not True.')
    print('Hello')

Obs: The first true condition will be executed. If none is True, else will be executed.

Example:

entrance = input('You want to "enter" or "exit"? ')

if entrance == 'enter':
    print('You have entered in the system!')

    print(12341234)
elif entrance == 'exit':
    print('You left the system!')
else:
    print('You didn\'t type "enter" or "exit".')

print('Out of the Blocks!')

Example:

condition1 = True
condition2 = True
condition3 = True
condition4 = True

if condition1:
    print('Code for condition 1')
    print('Code for condition 1')
elif condition2:
    print('Code for condition 2')
elif condition3:
    print('Code for condition 3')
elif condition4:
    print('Code for condition 4')
else:
    print('No conditions were met.')

if 10 == 10:
    print('Other if')

print('Out of if')
"""

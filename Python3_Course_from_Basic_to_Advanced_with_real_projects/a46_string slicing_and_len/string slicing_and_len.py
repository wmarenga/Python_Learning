"""
!String slicing_and_len
012345678
Hello World
-987654321
slicing [start:end:step] [::]
Note.: The len function returns the number of characters in the str.

Note.: The last index is not included (positive => left to right or negative => right to left).
*Example:
num = '01234'
print(num[0:4]) => '0123'
print(num[-5:-1]) => '0123'

variable = 'Hello World'
print(variable[::-1])

* Quantity of characters (len):

Counts the elements of a str, list, set, tuple, dict.

Note: Does not work with numeric types (int, float and bool).
Note: The return of len is an int (TypeError).

while True:
    user = input('Inform your user name: ')
    characters = len(user)
    if characters < 6:
        print(f'You need to enter at least {characters} characters.')
    else:
        print('You have been registered in the system.')
        print(user, characters, type(characters))
"""
string1 = input('Type something: ')
string2 = input('Type something else: ')

print(
    f'The total number of characters entered was: {len(string1) + len(string2)}')

print(len(string2))
print(string2.__len__())

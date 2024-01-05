"""
Logical Operators:

and     => All conditions need to be True for it to be True.
or      => or (one or the other has to be True to be True).
not     => No (value inverter)
in      => is in
not in  => is not in

* Example (Basic password validation system.):

entry = input('[E]ntry e[X]it: ')
entered_password = input('password: ')

allowed_password = '123456'

if entry == 'E' and entered_password == allowed_password:
    print('Entry')
else:
    print('Exit')

* Example of and:
a = 2
b = 2
c = 3
print(a == b and b < c)  # True (True and True)
print(a == b and b > c)  # False (True and False)
print(a != b and b < c)  # False (False and True)
print(a != b and b > c)  # False (False and False)

* Example of or:
print(a == b or b < c)  # True (True or True)
print(a == b or b < c)  # True (True or False)
print(a != b or b < c)  # True (False or True)
print(a != b or b > c)  # False (False or False)

* Other example:
entry = input('[E]ntry e[X]it: ')
entered_password = input('password: ')

allowed_password = '123456'

if (entry == 'E' or entry == 'e') and entered_password == allowed_password:
    print('Entry')
else:
    print('Exit')

* Short circuit assessment:
password = input('password: ') or 'without password'
print(password)

! Returns the first True value.
print(0 or False or 0 or 'abc' or True) # 'abc'

* Example of not:
a=1
b=2
c=3
print(not c > a)  # False (c > a == True) inverted would be False.
print(not c < b)  # True (c < b == False) inverted would be True.

if not a:
    print('Please fill in the value of A.')

if not b:
    print('Please fill in the value of B.')

if not c:
    print('Please fill in the value of C.')

* Example of in:
name = 'Luiz Otávio'

if 'u' in name:
    print('There is the letter "u" in your name.')

if 'otá' in name:
    print('There is')
else:
    print('There isn\'t.')

* Another example:
name='Wellington'
print(name[2]) # starts from left to right (positive). (0 1 2 3 4 5 6 7 8 9 10)
Output: 'l'

print(name[-10]) # starts from right to left (negative). (- 10 -9 -8 -7 -6 -5 -4 -3 -2 -1)
print(name[-len(name)])
Output: 'W'

* Example of not in:
name = 'Luiz Otávio'

if 'vio' not in name:
    print('I executed.')
else:
    print('There is the text.')

* Other example:
name = input('Entry your name: ')
find = input('Inform what do you want to find: ')

if find in name:
    print(f'{find} is in {name}.')
else:
    print(f'{find} is not in {name}.')

! falsy

If any value is considered false, the entire expression will be
evaluated at that value that is considered falsy (which you have
already seen): 0, 0.0, '', False.
There is also the None type which is used to represent a non-value.

* Short circuit assessment:

print(True and False and True)
print(True and 0 and True)
print(bool(0)) # False
print(bool(0.0)) # False
print(bool('')) # False
print(bool(None)) # False

print(bool(' ')) # True

a = ''    # Considered bool False
b = 0     # Considered bool False
c = 0.0   # Considered bool False
"""
variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)

"""
Operators in Python are:

+, -, *, /, //, **, %, ()

Precedence (1-most priority => 8-least priority):

Official:
https://docs.python.org/3/reference/expressions.html#operator-precedence

1) ()
2) **
3) *, /, //, %
4) +, -
5) ==, !=, <=, >=, >, <
6) not (bool)
7) and (bool)
8) or (bool)

() => They are used to change precedence in a mathematical expression
(ordination).

Example:
print(2 * (2 + 2)) # Output 8
print((2 * 2) + 3) # Output 7
print(1 + 1 ** 5 + 5) # Output 7

+ => Adds values (int, float) or concatenates (str);

Example:
print('Sum + => 10 + 10 = ', 10 + 10)

addition = 10 + 10
print('addition', addition)

# It will concatenate the strings '1010'.
print('Sum + => '10' + '10' = ', '10' + '10')

# It will generate an error, as we cannot join a str with an int.
print('Sum + => '10' + 2 = ', '10' + 2)

# Concatenating str + int with casting.
print('Wellington' + ' ' + 'Marenga has ' + str(51) + ' years.')

- => Subtract values;

Example:
print('Subtraction - => 10 - 5 = ', 10 - 5)

Subtraction = 10 - 5
print('Subtraction', Subtraction)

* => Multiplies values (numbers or str);

Example:
print('Multiplication * => 10 x 10 = ', 10 * 10)

Multiplication = 10 * 10
print('Multiplication', Multiplication)

# It will display an error.
print('Multiplication * => '10' x '10' = ', '10' * '10')

# It will repeat the str 10 times.
print('Multiplication * => '10' x 10 = ', '10' * 10)

/ => Normal division;

Example:
print('Division / => 10 / 2 = ', 10 / 2)  # Returns a float number always

Division = 10 / 3  # float
print('Division', Division)

`// => Integer division;

Example:
print(10.5 // 3)  # Returns a float number.
print(10 // 3)  # Returns an int number.
print(13 // 2)  # Returns an int number.

integer_division = 10 // 3
print('Integer division', integer_division)

** => Exponentiation or potentiation;

Example:
print(2 ** 10)

exponentiation = 2 ** 10
print('Exponentiation', exponentiation)

&  => Returns the modulus, remainder of dividing one number by another;

Example:
print(10 % 5)  # The result is 0, as it is the rest of the division.
print(10 % 3)  # The result is 1, as it is the rest of the division.

module = 55 % 2  # rest of Division
print('Module', module)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)

Example of Polyformism (acts differently in a given situation):
print(20 * 'A')  # 'AAAAAAAAAAAAAAAAAAAA'
print('20' + 'A')  # Output '20A'
print('20' + int(20))  # Output '2020'
"""

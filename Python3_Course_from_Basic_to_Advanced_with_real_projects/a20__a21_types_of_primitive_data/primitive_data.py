"""
Data Types:

Obs: We use the type() class within the print() function to
check the data type. The type function shows the type that
Python inferred from the value.

print(type('Otávio'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))

str   => string (texts -> 'Like this', "Like this")
print('Assim', type('Like this'))
print('123456', type('123456'))

int   => integers (numbers without dot -> 123456, 10, 20, 33, -11)

The int type represents any positive or negative number. Unsigned int
is considered positive.

print(11)
print(-11)
print(0)
print(123456, type(123456))
print(-33, type(-33))

float => Real number with floating point (numbers with dot -> 1.234, -12.13)

The float type represents any positive or negative floating point number.
Unsigned float is considered positive.

print(-12.11, type(-12.11))
print(11.44, type(11.44))
print(1.1, 10.11)
print(0.0, -1.5)

Obs: In programming languages we do not use commas to define real numbers.

bool  => boolean, logic ou binary (True or False)

When questioning something in a program, there are only two possible
answers: Yes (True) or No (False).

bool()  => print(bool([])), print(bool(0)), print(bool(''))

Obs: Some values evaluate to False and others evaluate to True.

Example:
False  => print(bool([])), print(bool(0)), print(bool(''))
True   => print(bool([1])), print(bool('abc')), print(bool(10 == 10))

There are several operators to "question".
Among them is ==, which is a logical operator that asks whether one value
is equal to another.

print(10 == 10)  # Yes => True
print(10 == 11)  # No => False
print(10!=10, type(10!=10))
print(type(True))
print(type(False))

Type Cast (casting):

str()   => print(str('my name'))
int()   => print(int(1234)), print(int(10.10)), print(int(-12.12)), 
print(int('10')), print(int('10') + int('10'))

Obs: Even if we add the . we will still have an integer, where
numbers after the dot will be ignored.

float() => print(float(55.22)), print(float(33)), print(float(-77)),
           print(float('56.12'))

Obs: Even after adding an integer and casting it as float(), the zero
will be added after the point, making the value real.

"""
# Exercise:
# Create a registration and display it on the screen.
name = str(input('Type your name: ')).capitalize()
age = int(input('Type your age: '))
height = float(input('How tall are you in meters? '))

print(f'Your name is: {name}. Your name class is:: {type(name)}')
print(f'You are {age} years old. Your age class is: {type(age)}')
print(
    f'Your height is {height:.2f} meters. Your height class is: {type(height)}')

# Most Advanced Way

# Returning True ou False
print(
    f'You are of legal age: {True if age > 18 else False}. The class of your comparison is: {type(True if age > 18 else False)}')
# Returning converting to: Yes or No
print(
    f'You are of legal age: {"Yes" if (True if age > 18 else False) == True else "No"}. The class of your comparison is: {True if age > 18 else False}')

# Most Basic Way:

if age > 18:
    print(
        f'You are of legal age: {age > 18}. The class of your comparison is: {type(age > 18)}')
else:
    print(
        f'You are of legal age: {age < 18}. The class of your comparison is: {type(age < 18)}')

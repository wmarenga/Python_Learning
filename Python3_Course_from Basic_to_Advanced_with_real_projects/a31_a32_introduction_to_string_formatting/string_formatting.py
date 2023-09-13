name = 'Luiz'
age = 32
height = 1.80
is_legal_age = age > 18
Weight = 80
# bmi= Weight / (height * height)
bmi = Weight / (height ** 2)

# Using f-strings:
print(f'The {name} has {age} years old and your BMI is {bmi:.2f}.')

# Using the format():
print('{} has {} years old and your BMI is {:.2f}.'.format(name, age, bmi))

# Obs: We have to follow the same order as the parentheses.

# If we want to change the order, we have to insert sequential numbers inside the (indexed) parentheses.

print('{0} has {2:.2f} years old and your BMI is {1}.'.format(name, age, bmi))

# If we want to change the order, we have to insert named parameters inside the parentheses.
print('{i} has {n} years old and your BMI is {im:.2f}.'.format(
    n=name, i=age, im=bmi))

# Another way
a = 'AAAAA'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'
using_format = string.format(a, b, c)
print(using_format)

# Defining the order with numbers (index)
string = 'a={0} b={2:.2f} c={1}'
using_format = string.format(a, b, c)
print(using_format)

# Naming the parameters (named parameter)
# obs: When I name a parameter, everything that comes after it must be named.
# obs2: name3 => parameters (refers to the variable name), =c => argument (refers to the value of c).
string = 'a={name1} b={name2} c={name3:.2f}'
using_format = string.format(name1=a, name2=b, name3=c)
print(using_format)

# As only the last parameter was named, the others are positional.
string = 'a={} b={} c={name3:.2f}'
using_format = string.format(a, b, name3=c)
print(using_format)

# format is a method.

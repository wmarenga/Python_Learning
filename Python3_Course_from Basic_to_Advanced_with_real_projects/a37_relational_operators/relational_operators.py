"""
Comparison operators (relational):

OP      Meaning         Examplo (True)
>       bigger               2 > 1
>=      bigger or equal      2 >= 2
<       smaller              1 < 2
<=      smaller or equal     2 <= 2
==      equal               'a' == 'a'
!=      different           'a' != 'b'

print(2 == 2)  # True
print(2 != 2)  # False

num_1 = 2  # int
num_2 = '2'  # str

# Visually they are the same, but num_1 is an int and num_2 is str.
print(num_1, num_2)

print(num_1 == num_2)  # False

num_3 = 3
num_4 = 4

expression = num_3 <= num_4
print(expression)

var_1 = 'Luiz'
var_2 = 'Otávio'

expression_2 = (var_1 != var_2)
print(expression_2)

name = input('What is your name? ')
age = int(input('How old are you?'))

# Limit for taking out a loan
younger_age = 20  # too young
legal_age = 30  # not young

if age >= younger_age and age <= legal_age:
    print(f'{name} can take the loan.')
else:
    print(f'{name} can't take the loan.')

* How to open Python's interactive shell in the terminal.
***absolute path***
python -i "J:\Github\Dev_and_DataScience_Learning\Python_Learning\Python3_Course_from Basic_to_Advanced_with_real_projects\a37_relational_operators/relational_operators.py"
***relative path***
python -i ".\\Python3_Course_from Basic_to_Advanced_with_real_projects\\a37_relational_operators\\relational_operators.py"
"""
print("Hello")

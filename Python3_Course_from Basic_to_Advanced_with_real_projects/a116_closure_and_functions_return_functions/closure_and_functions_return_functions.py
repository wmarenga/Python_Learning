"""
Closure and functions that return other functions
"""


def create_greeting(greeting):
    def greet(name):
        return f'{greeting}, {name}!'
    return greet


say_good_morning = create_greeting('Bom dia')
say_good_night = create_greeting('Boa noite')

for name in ['Maria', 'Joana', 'Luiz']:
    print(say_good_morning(name))
    print(say_good_night(name))

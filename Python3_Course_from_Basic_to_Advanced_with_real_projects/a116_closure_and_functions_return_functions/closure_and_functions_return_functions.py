"""
Closure and functions that return other functions
"""


def create_greeting(greeting):
    def greet(name):
        return f'{greeting}, {name}!'
    # By removing the parentheses from the function return
    # we are only returning the function itself, without executing it.
    return greet


say_good_morning = create_greeting('Good_morning')
say_good_night = create_greeting('Good_night')

for name in ['Maria', 'Joana', 'Luiz']:
    print(say_good_morning(name))
    print(say_good_night(name))

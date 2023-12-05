# decorator functions and Decorator
# to decorate = to add / to remove/ to restrict / to change
# Decorator functions are functions that decorate other functions
# Decorators are used to make Python use decorator functions in other functions.

def create_function(func):
    def internal_function(*args, **kwargs):
        print('I will decorate you.')
        for arg in args:
            not_string(arg)
        result = func(*args, **kwargs)
        print(f'Your result was {result}.')
        print("Okay, now you've been decorated.")
        return result
    return internal_function


def inverting_string(string):
    return string[::-1]


def not_string(param):
    if not isinstance(param, str):
        raise TypeError('parameter must be a string')


inverte_string_checking_parameter = create_function(inverting_string)
inverted = inverte_string_checking_parameter('123')
print(inverted)

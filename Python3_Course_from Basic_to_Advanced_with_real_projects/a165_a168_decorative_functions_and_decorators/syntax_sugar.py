# Decorators are "Syntax Sugar":

def create_function(func):
    def internal_function(*args, **kwargs):
        print('I will decorate.')
        for arg in args:
            not_string(arg)
        result = func(*args, **kwargs)
        print(f'Your result was {result}.')
        print("Okay, now you've been decorated")
        return result
    return internal_function


@create_function
def invert_string(string):
    print(f'{invert_string.__name__}')  # internal_function
    return string[::-1]


def not_string(param):
    if not isinstance(param, str):
        raise TypeError('parameter must be a string')


inverted = invert_string('123')
print(inverted)

# Decorators order:
def decorator_parameters(name):
    def decorator(func):
        print('The decorator:', name)

        def your_new_function(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {name}'
            return final
        return your_new_function
    return decorator


@decorator_parameters(name='5')
@decorator_parameters(name='4')
@decorator_parameters(name='3')
@decorator_parameters(name='2')
@decorator_parameters(name='1')
def my_sum(x, y):
    return x + y


ten_plus_five = my_sum(10, 5)
print(ten_plus_five)

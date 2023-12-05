# Free variables + nonlocal (locals, globals)
# print(globals())
# def outside(x):
#     a = x  # Free variables (not defined into the "inside" function).

#     def inside():
#         # print(locals())
#         print(inside.__code__.co_freevars)  # Check locals variables we can access.
#         return a + a
#     return inside


# inside1 = outside(10)
# inside2 = outside(20)

# print(inside1())
# print(inside2())


def concatenate(initial_string):
    final_value = initial_string

    def internal(value_to_concatenate=''):
        nonlocal final_value
        final_value += value_to_concatenate
        return final_value
    return internal


c = concatenate('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)

# Positional-Only Parameters (/) e Keyword-Only Arguments (*)

# *args (unlimited number of positional arguments)
# **kwargs (unlimited named arguments)

# 🟢 Positional-only Parameters (/) - Everything before
# the slash must be ❗️positional ONLY❗️.

# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/

# 🟢 Keyword-Only Arguments (*) - * alone ❗️DON’T SUCK❗️ values.

# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/


# !Using / to avoid positional arguments (not named):

# def my_sum(a, b, /):
#     print(a + b)


# my_sum(1, b=2)  # b must be positional before the /

# !After / we can use named arguments of positional:


# def my_sum2(a, b, /, x, y):
#     print(a + b + x + y)


# # b must be positional before the /
# # After / you can use named of positional (x, y)
# my_sum2(1, 2, 3, y=2)

# !Example (args):


# def my_sum3(a, b, *args):
#     print(args)  # ('test1', 'test2')
#     print(a + b)  # 6


# my_sum3(1, 2, 'test1', 'test2')

# !Example (kargs):

# After * you must use only named arguments.
def my_sum4(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)


my_sum4(1, 2, c=3, name='test')

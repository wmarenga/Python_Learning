"""
As we only import the module once, on some occasions we could
reload the module in order to update possible changes to variables
in the module. If the import is not reloaded, the variable would
retain its previous value.
"""
import importlib

import lesson_a156_m

print(lesson_a156_m.my_variable)

for i in range(10):
    importlib.reload(lesson_a156_m)  # reloading the module multiple times
    print(i)

print('End')

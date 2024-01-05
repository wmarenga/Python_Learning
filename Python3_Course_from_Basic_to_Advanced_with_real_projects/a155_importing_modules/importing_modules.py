"""
Modularization - Understanding your own Python modules.
The first module executed is called __main__.
You can import another entire module or part of the module.
Python knows the folder where __main__ is and the folders below it.
It does not recognize folders and modules above __main__ by default.
Python knows all modules and packages present in the sys.path paths.
"""
# In the path of sys.path

import lesson_a155_m
from lesson_a155_m import mysum, module_variable

print('This module is called', __name__)
# print('This module is called', __name__)
print(lesson_a155_m.module_variable)
print(module_variable)
print(mysum(2, 3))
print(lesson_a155_m.mysum(2, 3))

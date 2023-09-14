"""
Flag - Mark a location
None = No value
is and is not = is or not is (type, value, identity)
id = Identidade

*Example:
v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

Note: Python in some systems tries to assign the same id to different
variables with the same value assigned to them.
"""
condition = False
passed_in_the_if = None

if condition:
    passed_in_the_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passed_in_the_if is None:
    print('Não passou no if')
else:
    print('Passou no if')

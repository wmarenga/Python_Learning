"""
Iterating strings with while
"""
#       012345678910
name = 'Luiz Otávio'  # Iterables
#      1110987654321
name_size = len(name)
# print(name)
# print(name_size)
# print(name[3])

new_string = ''
# new_string += '*L*u*i*z* *O*t*á*v*i*o'
index = 0

while index < name_size:
    new_string += '*' + name[index]
    index += 1
print(new_string)

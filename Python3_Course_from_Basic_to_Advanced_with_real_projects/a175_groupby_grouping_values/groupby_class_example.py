from itertools import groupby, tee

students = [
    {'name': 'Luiz', 'grades': 'A'},
    {'name': 'Letícia', 'grades': 'B'},
    {'name': 'Fabrício', 'grades': 'A'},
    {'name': 'Rosemary', 'grades': 'C'},
    {'name': 'Joana', 'grades': 'D'},
    {'name': 'João', 'grades': 'A'},
    {'name': 'Eduardo', 'grades': 'B'},
    {'name': 'André', 'grades': 'C'},
    {'name': 'Anderson', 'grades': 'B'},
]


def order(item):
    return item['grades']


grouped_students = sorted(students, key=order)
groups = groupby(grouped_students, key=order)

for key, group in groups:
    print(key)
    for student in group:
        print(student)


#! Using lambda function
# grouped_students = sorted(students, key=lambda a: a['grades'])
# order = lambda item: item['grades']
# students.sort(key=order)
# grouped_students = groupby(students, order)

'''
#! Without tee (with list):

for grouping, grouped_values in grouped_students:
  values = list(grouped_values)
  print(f'grouping: {grouping}')
  for students in values:
    print(f'\t{student}')
  quantity = len(values)
  print(f'\t{quantity} students have grades {grouping}')
'''

#! With tee
# for grouping, grouped_values in grouped_students:
#     v1, v2 = tee(grouped_values)

#     print(f'grouping: {grouping}')

#     for student in v1:
#         print(f'\t{student}')

#     quantity = len(list(v2))
#     print(f'\t{quantity} students have grades {grouping}')

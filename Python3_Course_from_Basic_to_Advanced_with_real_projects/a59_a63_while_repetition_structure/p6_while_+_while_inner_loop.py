"""
while + inner while
"""
qt_lines = 5
qt_columns = 5

lines = 1
while lines <= qt_lines:
    column = 1
    while column <= qt_columns:
        print(f'{lines=} {column=}')
        column += 1
    lines += 1


print("It's Over!")

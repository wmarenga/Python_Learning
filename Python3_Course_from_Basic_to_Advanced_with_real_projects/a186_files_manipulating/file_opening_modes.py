# Read too: https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
# with open (context manager) and useful methods of TextIOWrapper
# We use the open function to open a file in Python (it may or may not exist).

# #
# file.close()

# with open(file_path, 'w+') as file:
#     file.write('line 1\n')
#     file.write('line 2\n')
#     file.writelines(
#         ('line 3\n', 'line 4\n')
#     )
#     file.seek(0, 0)
#     print(file.read())
#     print('reading')
#     file.seek(0, 0)
#     print(file.readline(), end='')
#     print(file.readline().strip())
#     print(file.readline().strip())

#     print('READLINES')
#     file.seek(0, 0)
#     for line in file.readlines():
#         print(line.strip())


# print('#' * 10)

# with open(file_path, 'r') as file:
#     print(file.read())

file_path = r"J:\\Github\\Dev_and_DataScience_Learning\\Python_Learning\\Python3_Course_from_Basic_to_Advanced_with_real_projects\\a186_files_manipulating\\abc.txt"

with open(file_path, 'w+', encoding='utf8') as file:
    file.write('Attention\n')
    file.write('line 1\n')
    file.write('line 2\n')
    file.writelines(
        ('line 3\n', 'line 4\n')
    )
    file.seek(0, 0)
    print(file.read())
    print('reading')
    file.seek(0, 0)
    print(file.readline(), end='')
    print(file.readline().strip())
    print(file.readline().strip())

    print('READLINES')
    file.seek(0, 0)
    for line in file.readlines():
        print(line.strip())


print('#' * 10)

with open(file_path, 'r') as file:
    print(file.read())

# Read too: https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
# with open (context manager) and useful methods of TextIOWrapper
# We use the open function to open a file in Python (it may or may not exist).

import json
import os

# !Modos:
# r (reading), w (writing), x (for creation)
# a (write at the end), b (binary)
# t (text mode), + (reading and writing)
# Context manager - with (open and close)

# !Useful methods
# write, read (write and read)
# writelines (write several lines)
# seek (move the cursor)
# readline (read line)
# readlines (read lines)

# !Let's talk more about the os module, but:
# os.remove or unlink - delete the file
# os.rename - change the name or move the file

# !Let's talk more about the json module, but:
# json.dump = Generate a json file
# json.load

# !Example 1

# !Another way:
base_dir = os.path.dirname(__file__)
save_to = os.path.join(base_dir, 'file_name.json')

file_path = r"J:\\Github\\Dev_and_DataScience_Learning\\Python_Learning\\Python3_Course_from_Basic_to_Advanced_with_real_projects\\a186_a190_files_manipulating\\abc.txt"

# file = open(file_path, 'w')
# #
# file.close()

# with open(file_path, 'w+') as file:
#     file.write('Line 1\n')
#     file.write('Line 2\n')
#     file.writelines(
#         ('Line 3\n', 'Line 4\n')
#     )
#     file.seek(0, 0)
#     print(file.read())
#     print('Reading')
#     file.seek(0, 0)
#     print(file.readline(), end='')
#     print(file.readline().strip())
#     print(file.readline().strip())

#     print('READLINES')
#     file.seek(0, 0)
#     for Line in file.readlines():
#         print(Line.strip())


# print('#' * 10)

# with open(file_path, 'r') as file:
#     print(file.read())

with open(file_path, 'w', encoding='utf8') as file:
    file.write('Attention\n')
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.writelines(
        ('Line 3\n', 'Line 4\n')
    )

# os.remove(file_path) # or unlink (delete the file)
# os.rename(file_path, 'abc.txt') # we can rename or move the file to another folder.

# ?os.rename(current_file_path, new_file_path)

# !Example 2

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

# w  => opens the file, delete everything, write something (file.write or writelines) and save (without reading).
# w+ => In addition to doing the "w" steps, it also enables reading.
# a+ => add things to the end of the last line (append).
# b  => opens the file in binary mode (raw).


with open(file_path, 'w', encoding='utf8') as file:
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

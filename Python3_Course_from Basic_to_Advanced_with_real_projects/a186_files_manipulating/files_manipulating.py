"""
Documentation:
https://docs.python.org/3/library/functions.html#open

# !Creating files with Python + Context Manager with

# !We use the open function to open a file in Python (it may or may not exist):

Modes:
r (reading), w (writing), x (for creation)
a (write at the end), b (binary)
t (text mode), + (Reading and writing)

# !Context manager - with (open and close):

# !Useful methods:
write, read (write and read)
writelines (write several lines)
seek (move the cursor)
readline (read line)
readlines (read lines)

# !Let's talk more about the os module, but:
os.remove or unlink -> delete the file
os.rename -> change the name or move the file

# !Let's talk more about the json module, but:
json.dump = Generate a json file
json.load

complete_path_mac_linux = '/Users/lesson116.txt'
complete_path_windows = r'C:\\Users\\new\\lesson116.txt'
file_path = 'lesson116.txt'

file = open(file_path, 'w')

file.close()

# !Context manager (The file will be open and closed automatically):

with open(file_path, 'w') as file:
    print('Hello')
    print('file will be closed.')

# !Creating a file for reading and writing:

file = open(r"J:\\Github\\Dev_and_DataScience_Learning\\Python_Learning\\Python3_Course_from Basic_to_Advanced_with_real_projects\\a186_files_manipulating\\abc.txt", 'w+')
file.write('line 1\n')
file.write('line 2\n')
file.write('line 3\n')

file.seek(0, 0)  # Return the cursor to its initial position

# !Reading the file
print('reading lines: ')
print(file.read())

print('##################')
file.seek(0, 0)  # Return the cursor to the beginning again

# !Reading line by line
print(file.readline(), end='')  # Do not send line breaks
print(file.readline().strip())  # Do not send line breaks (other way)

# !Using for:
for line in file.readlines():
    print(line.strip())

print('##################')

file.seek(0, 0)  # Return the cursor to the beginning again
print(file.readlines())  # Display a list of all lines

file.close()  # It is very important to always close the file.

# !Using the try block:

from asyncore import write


try:
    file = open(r"J:\\Github\\Dev_and_DataScience_Learning\\Python_Learning\\Python3_Course_from Basic_to_Advanced_with_real_projects\\a186_files_manipulating\\abc.txt", 'w+')
    file.write('line')
    file.seek(0)
    print(file.read())
finally:
    file.close()

# !More Pythomic way, as it opens and closes the file automatically:

with open(r"J:\\Github\\Dev_and_DataScience_Learning\\Python_Learning\\Python3_Course_from Basic_to_Advanced_with_real_projects\\a186_files_manipulating\\abc.txt", 'w+') as file:
    # file.write('line 1\r\n') # Windows
    file.write('line 1\n')  # MacOS
    file.write('line 2\n')
    file.write('line 3\n')
    file.writelines(
        ('line 4\n', 'line 5\n')
    )
    file.seek(0, 0)
    print(file.read())

# !Just reading the contents of the file (r):

with open(r"J:\\Github\\Dev_and_DataScience_Learning\\Python_Learning\\Python3_Course_from Basic_to_Advanced_with_real_projects\\a186_files_manipulating\\abc.txt", 'r') as file:
    print(file.read())

# !Activate the function to add things to file => append (a+):

with open(r"J:\\Github\\Dev_and_DataScience_Learning\\Python_Learning\\Python3_Course_from Basic_to_Advanced_with_real_projects\\a186_files_manipulating\\abc.txt", 'a+') as file:
    file.write('Other line\n')
    file.seek(0, 0)
    print(file.readline())

# !Removing the file:

import os
os.remove(r"J:\\Github\\Dev_and_DataScience_Learning\\Python_Learning\\Python3_Course_from Basic_to_Advanced_with_real_projects\\a186_files_manipulating\\abc.txt")

"""
# !Creating and manipulating json files:

import json

d1 = {
    'person 1': {
        'name': 'Luiz',
        'age': 25,
    },
    'person 2': {
        'name': 'Rose',
        'age': 30,
    },
}
print(d1)

# !Converting to json:
d1_json = json.dumps(d1, indent=True)

with open('a186_files_manipulating/abc.json', 'w+') as file:
    file.write(d1_json)

"""
Python lists => type: list():
- Supports various values of any type;
- Reusable Knowledge - Indexes and Slicing;

Useful Methods:
    append - Add an item at the end
    insert - Adds an item to the chosen index => .insert(index, value)
    pop - Removes from the end or index chosen
    del - erases an index
    clear - cleans the list
    extend - extends the list
    + - concatenate lists

- min, max;
- range.
- type(list()) # Show the type

Create Read Update Delete = my_list[i] (CRUD)

text = 'value'
my_list = [1, 2, 3, 4, 'Luiz Otávio', True, 10.5, Class()]

Indexes
Positive   0     1       2    3    4     5
Negative  -6    -5      -4   -3   -2    -1

my_list = ['A', 'cool', 'C', 'D', 'E', 10.5]

An item at a list supports multiple values, while
the indexes of a string only support a value.

* Example (accessing a string inside a list):

print(my_list[1][0:3])

* Example:

print(my_list[1]) # Output: 'cool'
print(my_list[-5]) # Output: 'cool'

Indexes

Positive 0123456789
Negative -8-7-6-5-4-3-2-1

string = 'AcoolCDE'

* Example:
print(string[1]) # Output: 'c'
print(string[-8]) # Output: 'A'

# Changing an index of a string

* Example:
my_list[5] = 'Anything else'
# print(my_list)

# Showing a interval of items from a my_list:

* Example:
print(my_list[0:3])
print(my_list[:4])  # by default the start is zero
print(my_list[2:])  # from index 2 to the end
print(my_list[2::2])  # from index 2 to the end of 2 to 2.
print(my_list[:-1:2])  # from the last item to the beginning of 2 to 2.
print(my_list[::-1])  # Reversing my_list

l1 = [1, 2, 3]
l2 = [4, 5, 6]

Using +:

* Example:
my_lists = l1 + l2  # concatenate: my_lists, l1 and l2
print(l1)
print(l2)
print(my_lists)

Using extend (extending the l1 with l2)

* Example:
l1.extend(l2)
print(l1)
print(l2)

Using append (Insert a new value at the end of my_list)

* Example:
l2.append('b')
print(l1)
print(l2)

Using Insert to add values anywhere in My_List

* Example:
l2.insert(0, 'banana')
print(l2)

Deleting elements from the end of a my_list (pop ())

* Example:
l2 = [4, 5, 6]
l2.insert(0, 'banana')
print(l2)
l2.pop()
print(l2)

Excluding values with del

#     0  1  2  3  4  5  6  7  8
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l2)

* Example:
del (l2[3:5])  # excluding by slicing [4, 5]
print(l2)

l2.insert(0, 'Banana')
print(l2)

del(l2[0])
print(l2)

* Example:

#        0   1   2   3   4   5
my_list = [10, 20, 30, 40]
my_list[2] = 300
del my_list[2]
del my_list[-1] # Deleting the last item from the list
print(my_list)
print(my_list[2])
my_list.append(50) # Add item in the last position of the list
my_list.pop() # Removes the last item from the list
my_list.append(60)
my_list.append(70)
last_value = my_list.pop(3) # Removing elements of a specific index
print(my_list, 'removed,', last_value)

"""
# Display the highest value of my_list with max

# * Example:
#     0  1  2  3  4  5  6  7  8
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(l2))
print(min(l2))

# Creating my_list more easily with (range () and list ())

# * Example:
l3 = list(range(1, 10))  # [1, 2, 3, 4, 5 ,6 ,7 ,8, 9]
l3 = list(range(0, 100, 8))  # With intervals

for value in l3:
    print(value, end=', ')

# Accumulating 8 to the next number

my_sum = 0
accumulating = list()
for value in l3:
    my_sum += value
    accumulating.append(my_sum)

print(accumulating)

# Check the types of each element of a my_list

l4 = ['String', True, 10, -20.5]

for elem in l4:
    print(f'Your element is {elem} and your type is {type(elem)}.')

# for in with lists

# * Example

my_list = ['Maria', 'Helena', 'Luiz']

for name in my_list:
    print(name, type(name))

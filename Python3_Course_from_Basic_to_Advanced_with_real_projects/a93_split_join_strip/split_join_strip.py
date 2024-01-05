"""
Split and join with list and str in Python:

- split     => It has the function of dividing a string (str);
- join      => It has the function of joining a list (str);

"""
# # *Example 1 (Creating a list from a string by spaces):
# string = 'Brazil is the country of football, Brazil is five times winner.'
# my_list_1 = string.split(' ')  # by the blank spaces
# print(my_list_1)
# my_list_2 = string.split(',')  # by the commas
# print(my_list_2)

# # *Example 2 (Iterating over my_list 1):
# for n in my_list_1:
#     print(n)

# # *Example 3 (Counting words):
# for n in my_list_1:
#     print(f'The word {n} appeared {my_list_1.count(n)} times in the phrase.')

# # *Example 4:
# string = 'Brazil is the country of football, Brazil is five times winner.'
# my_list_1 = string.split(' ')

# word = ''
# counting = 0
# for n in my_list_1:
#     qtt_times = my_list_1.count(n)
#     if qtt_times > counting:
#         counting = qtt_times
#         word = n

# print(f'The word that appeared most often is: {word} => {counting} times')

# # *Examplo 5 (strip = Remove spaces from the beginning and end of the string):
# #! Note: lstrip (remove all left space)/ rstrip (remove all right space)
# string = 'Brazil is the country of football, Brazil is five times winner.'
# my_list_1 = string.split(' ')

# for n in my_list_1:
#     print(n.strip().capitalize())

# # *Examplo 6 (Inserting each word of a string into a list)
# string = 'Brazil is five times winner.'
# my_list = string.split(' ')
# # print(my_list)

# # *Examplo 7 (Creating a string with the elements of a my_list with (join))
# string2 = ' '.join(my_list)
# print(string2)

# * Example 8:
phrases = '   Look what   , interesting thing          '
my_list_raw_phrases = phrases.split(',')

my_list_phrases = []
for i, phrases in enumerate(my_list_raw_phrases):
    my_list_phrases.append(my_list_raw_phrases[i].strip())

print(my_list_raw_phrases)
print(my_list_phrases)
joined_phrases = ', '.join(my_list_phrases)
print(joined_phrases)

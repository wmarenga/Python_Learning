"""
Indexes
0123456789...........................33

If the element has indices, it means it is iterable.

# Iteration => Iterate

phrase = "The rat gnawed the cloth of the Rome's king."
phrase_size = len(phrase)
print(phrase_size)
print(phrase[5])

"""
phrase = "The rat gnawed the cloth of the Rome's king."
phrase_size = len(phrase)
counter = 0


# while counter < phrase_size:
#     print(phrase[counter], counter)
#     counter += 1


# Example creating a new variable with all uppercase strings.

new_string = ''

# while counter < phrase_size:
#    new_string += phrase[counter].upper()
#    counter += 1

# print(new_string)

# Example changing the letters chosen by the user to uppercase.

user_decision = input('Which letter do you want to capitalize: ')

while counter < phrase_size:
    letter = phrase[counter]
    if letter == user_decision:
        new_string += user_decision.upper()
    else:
        new_string += letter
    counter += 1

print(new_string)

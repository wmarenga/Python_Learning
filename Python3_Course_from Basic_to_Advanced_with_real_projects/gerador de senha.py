import string
import random

number_of_strings = 1
length_of_string = 13
for x in range(number_of_strings):
    print(''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits + string.punctuation) for _ in range(length_of_string)))

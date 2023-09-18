# frase.count('Python')
# Note: Inside of print(), I don't need \ to breal lines.

phrase = 'Python is a multi-paradigm programming language. '\
    'Python was created by Guido van Rossum.'

i = 0
qtt = 0
letter_that_appears_more = ''

while i < len(phrase):
    current_letter = phrase[i]

    if current_letter == ' ':
        i += 1  # By inserting this counter, we avoid an infinite loop.
        continue

    current_qtt = phrase.count(current_letter)

# If we use <: the largest first letter will be displayed.
# If we use <=: the second largest letter will be displayed.
    if qtt < current_qtt:
        qtt = current_qtt
        letter_that_appears_more = current_letter

    i += 1

print(
    'The letter that appeared most often was '
    f'"{letter_that_appears_more}" that appeared '
    f'{qtt} times'
)

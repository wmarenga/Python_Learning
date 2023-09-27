# Exercise - question and answer system


questions = [
    {
        'Question': 'How much is 2+2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'How much is 5*5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'How much is 10/2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]

right_answers = 0
for q in questions:
    print('Question:', q['Question'])
    print()
    options = q['Options']

    for i, op in enumerate(options):
        index_letters = ['a', 'b', 'c', 'd']
        print(f'{index_letters[i]})', op)
    choice = input('Choose one option: ')

    while True:
        confirmation_answer = q['Answer']
        if choice not in index_letters:
            choice = input('Choose only [a],[b],[c],[d]: ')
        else:
            if index_letters.index(choice) == options.index(confirmation_answer):
                right_answers += 1
                print('Right 👍')
                print()
            else:
                print('Wrong ❌')
                print()
            break


print('You got it right', right_answers)
print('in', len(questions), 'questions.')

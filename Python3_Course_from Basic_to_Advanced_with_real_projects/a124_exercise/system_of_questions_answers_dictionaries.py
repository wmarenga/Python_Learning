print()
print('Explanatory text')

questions = {
    'question 1': {
        'question': 'How much is 2+2? ',
        'answers': {'a': '1', 'b': '4', 'c': '5', },
        'right_answer': 'b',
    },
    'question 2': {'question': 'How much is 3x2? ',
                   'answers': {'a': '4', 'b': '101', 'c': '6', },
                   'right_answer': 'c',
                   },
}
print()

right_answer = 0
for question, data_questions in questions.items():
    print(f'{question}: {data_questions["question"]}')

    print('answers: ')
    for answer, data_answers in data_questions['answers'].items():
        print(f'[{answer}]: {data_answers}')

    user_answer = input('Your answer is: ')

    if user_answer == data_questions['right_answer']:
        print("EHHHHHH!!! You're right!!!!")
        right_answer += 1
    else:
        print('IXXIIIII!!! Sorry but you made a mistake!!!!')

    print()

questions_qtt = len(questions)
right_percentage = right_answer / questions_qtt * 100
print(f'You got {right_answer} answers right.')
print(f'Your hit percentage were {int(right_percentage)}%.')

questions = [
    {
        'question': 'How much is 2+2?',
        'options': ['1', '3', '4', '5'],
        'answer': '4',
    },
    {
        'question': 'How much is 5*5?',
        'options': ['25', '55', '10', '51'],
        'answer': '25',
    },
    {
        'question': 'How much is 10/2?',
        'options': ['4', '5', '2', '1'],
        'answer': '5',
    },
]


def start_game():
    print("*** Welcome to our question and answer game! ***")
    decision = input("Are you ready to start the game? [Y]es [N]o ").upper()
    right_answers = 0
    question_num = 1
    while decision not in 'YN':
        decision = input("Please enter only [Y]es [N]o ").upper()
    else:
        if decision == 'Y':
            for q in questions:
                print(f"Questions {question_num}:", q['question'])
                print()
                for i, v in q.items():
                    if i == 'options':
                        print(f"The options are: {v}", end='\n')
                        print()
                player_answer = input("What is your answer? ")
                question_num += 1
                if player_answer == v:
                    right_answers += 1
                else:
                    continue
            print(f"You got {right_answers} right answers.")
        else:
            print("See you later!")


start_game()

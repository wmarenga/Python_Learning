"""
Make a game for the user to guess which one the secret word.
- You will propose a secret word any and will give the possibility to
the user types only one letter.
- When the user types a letter, you will check if the typed letter is
in the secret word.
    > If the letter entered is in the secret word; display the letter;
    > If the letter entered is not in the secret word; display *.

At the end, count your attempts user.
"""
import os


secret_word = input("Type the secret word: ").lower()
correct_letters = ''
tries_number = 0

while True:
    guess_letter = input("Guess a letter: ")
    tries_number += 1

    if len(guess_letter) > 1:
        print("Please, type just one letter.")
        continue

    if guess_letter in secret_word:
        correct_letters += guess_letter

    formed_word = ''
    for guess_letter in secret_word:
        if guess_letter in correct_letters:
            formed_word += guess_letter
        else:
            formed_word += '*'

    os.system('cls')  # clean the Terminal
    print('Formed word: ', formed_word)

    if formed_word == secret_word:
        print('You WON!')
        print('The secret word is ', formed_word)
        print(f'You did it with {tries_number} tries.')
        try_again = input(
            'Do you want to try again? [Y]es/[N]o ').lower().startswith('y')
        if try_again:
            correct_letters = ''
            tries_number = 0
            secret_word = input("Type the secret word: ").lower()
        else:
            break

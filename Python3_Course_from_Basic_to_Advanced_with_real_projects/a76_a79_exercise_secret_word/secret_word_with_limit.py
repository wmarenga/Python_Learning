secret_word = 'perfume'
typed_letters = []
trials = 5

while True:
    if trials <= 0:
        print('You lose!!!')
        break

    letter = input('Type one letter: ')

    if len(letter) > 1:
        print("Ahhh that doesn't work, just type one letter.")
        continue

    typed_letters.append(letter)

    if letter in secret_word:
        print(f'UHUULLL, the letter "{letter}" exists in the secret word.')
    else:
        print(
            f'AFFFzzz: the letter "{letter}" does not exist in the secret word.')
        typed_letters.pop()

    secret_word_temporary = ''
    for secret_letter in secret_word:
        if secret_letter in typed_letters:
            secret_word_temporary += secret_letter
        else:
            secret_word_temporary += '-*-'

    if secret_word_temporary == secret_word:
        print(
            f"That's cool, YOU WON!!! The word was {secret_word_temporary}.")
        break
    else:
        print(f'The secret word looks like this: {secret_word_temporary}')

    if letter not in secret_word:
        trials -= 1

    print(f'You still have {trials} trials.')
    print()

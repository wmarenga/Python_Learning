"""
Exercise:
- Ask the user to enter their name;
- Ask the user to enter their age;
If name and age are entered:
    Display:
        Your name is {name};
        Your reversed name is {reversed name};
        Your name contains (or does not contain) spaces;
        Your name has {n} letters;
        The first letter of your name is {letter};
        The last letter of your name is {letter};
If nothing is entered for name or age:
    display "Sorry, you left fields empty."
"""
name = input("Inform your name: ")
age = input("Inform your age: ")
spaces = 0
first_name = ''
if name == '' or age == '':
    if name == '':
        print('Sorry, you fields name is empty.')
    else:
        print('Sorry, you fields age is empty.')
else:
    print(f'Your name is {name}.')
    print(f'Your reversed name is {name[::-1]}')
    for s in range(0, len(name)):
        if name[s] != " ":
            first_name += name[s]
        else:
            break
        if name[s] == " ":
            spaces += 1
    if spaces != 0:
        print(f'Your name contains {spaces} spaces')
    else:
        print('Your name does not contain spaces')
    print(f'Your name has {len(name)-spaces} letters')
    print(f'Your first name is: {first_name}.')
    print(f'The first letter of your name is {first_name[0]}')
    print(f'The last letter of your name is {first_name[-1]}')

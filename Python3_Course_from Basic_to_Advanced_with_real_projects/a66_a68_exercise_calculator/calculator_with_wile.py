""" Calcular with while """

# while True:
#     print('nummmmm')
#     #########
#     # lower() => convert to lowercase.
#     # startswith('s') => defines the letter that begins ('s') and convert to boolean.
#     decision = input('Do you want to exit? e[x]it: ').lower().startswith('x')

#     if decision is True:
#         break

while True:
    number_1 = input('Enter one number: ')
    number_2 = input('Enter another number: ')
    operador = input('Enter an operator (+-/*): ')

    valid_number = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(number_1)
        num_2_float = float(number_2)
        valid_number = True
    except:
        valid_number = None

    if valid_number is None:
        print('One or both of the numbers entered are invalid.')
        continue

    allowed_operators = '+-/*'

    if operador not in allowed_operators:
        print('Invalid operator.')
        continue

    if len(operador) > 1:
        print('Enter only one operator.')
        continue

    ###

    print("Calculating the result of your account.: ")
    if operador == "+":
        print(f"{num_1_float} + {num_2_float}= ", num_1_float + num_2_float)
    elif operador == "-":
        print(f"{num_1_float} - {num_2_float}= ", num_1_float - num_2_float)
    elif operador == "/":
        print(f"{num_1_float} / {num_2_float}= ", num_1_float / num_2_float)
    elif operador == "*":
        print(f"{num_1_float} * {num_2_float}= ", num_1_float * num_2_float)
    else:
        print("It should never get here.")

    decision = input('Do you want to exit? e[x]it: ').lower().startswith('x')

    if decision is True:
        break

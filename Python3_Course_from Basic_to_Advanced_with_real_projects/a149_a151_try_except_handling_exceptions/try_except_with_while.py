
def convert_number(value):
    try:
        value = int(value)
        return value
    except ValueError:
        try:
            value = float(value)
            return value
        except ValueError:
            pass


while True:
    number = convert_number(input('Type a number: '))
    if number is None:
        print('Error: This is not a number.')
    else:
        print(number * 2)

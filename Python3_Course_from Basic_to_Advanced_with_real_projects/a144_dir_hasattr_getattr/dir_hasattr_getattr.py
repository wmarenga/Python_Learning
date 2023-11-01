# dir, hasattr and getattr in Python
string = 'Luiz'
method = 'upper1'

# getattr => checks whether the method exists on the type.
if hasattr(string, method):
    print('Exist upper')
    print(string.upper())
    print(getattr(string, method)())
else:
    print('Not exist the method', method)

print(dir(string))  # show all attributes of the type.

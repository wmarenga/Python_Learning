value = True

# The pass or ... leave the code in holding (waiting for one future code).
# It doesn't generate an error, it just doesn't return anything.
if value:
    pass
else:
    print('Good bye!')

if value:
    ...
else:
    print('Good bye!')

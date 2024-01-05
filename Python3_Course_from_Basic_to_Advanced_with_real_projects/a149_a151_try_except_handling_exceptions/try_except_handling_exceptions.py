# (Part1) try and except to handle exceptions
# a = 18
# b = 0
# c = a / b

#! Example 1 => Basic example (shows any errors - not recommended):

# try:
#     print(a)
# except:
#     print('Erro!')

#! Example 2 (Part 1):

# try:
#     a = 18
#     b = 0
#     # print(b[0])
#     print('line 1'[1000])
#     c = a / b
#     print('line 2')
# except ZeroDivisionError:
#     print('Divided by zero.')
# except NameError:
#     print('Name b is not defined.')
# except (TypeError, IndexError):
#     print('TypeError + IndexError')
# except Exception:
#     print('UNKNOWN ERROR.')

# print('CONTINUE')

#! Example 3 (Part 2):

# try:
#     a = 18
#     b = 0
#     # print(b[0])
#     # print('line 1'[1000])
#     c = a / b
#     print('line 2')
# except ZeroDivisionError as e:
#     print(e.__class__.__name__)
#     print(e)
# except NameError:
#     print('Name b not defined.')
# except (TypeError, IndexError) as error:
#     print('TypeError + IndexError')
#     print('MSG:', error)
#     print('Name:', error.__class__.__name__)
# except Exception:
#     print('UNKNOWN ERROR.')

# print('CONTINUE')

#! Example 4 => More specific example handling with the error:

# try, except, else and finally
# https://docs.python.org/3/library/exceptions.html#built-in-exceptions

# ? The "FINALLY" will always be executed (The exception cannot be handled).
# ? The "ELSE" will be executed in case of the code executes without error.
# ? (as error) => saves the error in a variable (error).
# ? (e.__class__.__name__) => Captures the name of the error message in Python.

try:
    print('OPEN FILE')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDED BY ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print("IT IS NOT AN ERROR")
finally:
    print('CLOSE FILE.')

#! Example 5 => More specific example handling with the error:

# try:
#     print(a)  # NameError
#     a = []
#     print(a[1])  # IndexError
#     a = {}
#     print(a[1])  # KeyError
#     a = {}
# except NameError as error:  # NameError only
#     print('Developer error, talk to him.')
# except (IndexError, KeyError) as error:
#     print('Index or key error.')
# except Exception as error:  # catches any other errors in the code
#     print('An unexpected error occurred.')
# else:  # It will always be executed when the code has no error.
#     print('Your code has been executed successfully!')
#     print(a)
# finally:
#     print('It will be executed whether it has an error or not.')


# print("Let's continue...")

#! Example 6 =>  Method of handling exceptions by assigning a default value in case of an error.

# try:
#     a = 1/0
#     try:
#         a = 1/0
#     except:
#         print('Error')
# except NameError as error:  # NameError only
#     print('Developer error, talk to him.')
# except (IndexError, KeyError) as error:
#     print('Index or key error.')
# except Exception as error:  # catches any other errors in the code
#     print('An unexpected error has occurred.')
# else:  # It will always be executed when the code has no error.
#     pass
# finally:
#     a = None


# print(a)

"""
Make a shopping list with lists. The user must
have the possibility to insert, delete and list
values from your list. Do not allow the program
break with errors of non-existent indexes in the list.
"""
# Teacher Solution:

import os

my_list = []

while True:
    print('Choose an option')
    option = input('[i]insert [d]elet [l]ist: ')

    if option == 'i':
        os.system('cls')
        value = input('Value: ')
        my_list.append(value)
    elif option == 'a':
        index_str = input(
            'Choose the index to delete: '
        )

        try:
            index = int(index_str)
            del my_list[index]
        except ValueError:
            print('Please enter int number.')
        except IndexError:
            print('Index does not exist in my_list')
        except Exception:
            print('Unknown error')
    elif option == 'l':
        os.system('clear')

        if len(my_list) == 0:
            print('Nothing for my_listr')

        for i, value in enumerate(my_list):
            print(i, value)
    else:
        print('Please choose i, a or l.')

# import os


# my_shopping_list = []
# question = True

# while question:
#     question = input(
#         "Do you want to [I]nsert, [D]elet [S]how itens in your list? or [E]xit. ")[0].lower()
#     if question in ['i', 'd', 's', 'e']:
#         os.system('cls')
#         if question == "i":
#             product = input("Insert your product: ").lower()
#             if product not in my_shopping_list:
#                 my_shopping_list.append(product)
#                 continue
#             else:
#                 print("The product already exists in the list. Choose another product.")
#         elif question == "d":
#             question_del = input("Which item do you want to remove? ").lower()
#             if question_del in my_shopping_list:
#                 my_shopping_list.remove(question_del)
#                 print(f"You partial shopping list is: {my_shopping_list}")
#             else:
#                 print("Your item does not exist in the list.")
#                 print(
#                     f"Check you partial here: {my_shopping_list}")
#         elif question == "s":
#             print(f"You partial shopping list is: {my_shopping_list}")
#         elif question == "e":
#             break
#     else:
#         print(
#             "Please, Type only [I] to insert, [D] to delet, [S] to show or [E] to exit the list.")

# print(f"You final shopping list is: {my_shopping_list}")

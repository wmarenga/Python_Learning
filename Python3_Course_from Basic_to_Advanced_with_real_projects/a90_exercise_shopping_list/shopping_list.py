"""
Make a shopping list with lists. The user must
have the possibility to insert, delete and list
values from your list. Do not allow the program
break with errors of non-existent indexes in the list.
"""
# Teacher Solution:

import os

# my_list = []

# while True:
#     print('Choose an option')
#     option = input('[i]insert [d]elet [l]ist: ')

#     if option == 'i':
#         os.system('cls')
#         value = input('Value: ')
#         my_list.append(value)
#     elif option == 'd':
#         index_str = input('Choose the index to delete: ')

#         try:
#             index = int(index_str)
#             del my_list[index]
#         except ValueError:
#             print('Please enter int number.')
#         except IndexError:
#             print('Index does not exist in my_list')
#         except Exception:
#             print('Unknown error')
#     elif option == 'l':
#         os.system('clear')

#         if len(my_list) == 0:
#             print('Nothing for my_listr')

#         for i, value in enumerate(my_list):
#             print(i, value)
#     else:
#         print('Please choose i, a or l.')

# My code:
my_shopping_list = []


def consult_list(my_list):
    for index, value in enumerate(my_list):
        print(f"{index} => {value}")


while True:
    question = input(
        "Do you want to [I]nsert, [D]elet [S]how itens in your list? or [E]xit. ")[0].lower()
    if question in ['i', 'd', 's', 'e']:
        os.system('cls')
        if question == "i":
            product = input("Insert your product: ").lower()
            if product not in my_shopping_list:
                my_shopping_list.append(product)
                continue
            else:
                print("The product already exists in the list. Choose another product.")
        elif question == "d":
            question_del = input("Which item do you want to remove? ").lower()
            if question_del in my_shopping_list:
                my_shopping_list.remove(question_del)
                print(
                    f"The product {question_del} has been removed from your list.")
            elif my_shopping_list == []:
                print("Your list is empty.")
            else:
                print("Your item does not exist in the list.")
        elif question == "s":
            print("You partial shopping list is:")
            consult_list(my_shopping_list)
        elif question == "e":
            print("Your final shopping list is: ")
            consult_list(my_shopping_list)
            break
    else:
        continue

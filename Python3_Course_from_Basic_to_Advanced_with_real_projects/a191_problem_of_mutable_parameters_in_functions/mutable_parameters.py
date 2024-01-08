# Mutable: Lists, dictionaries
# The problem occurs with mutable objects (list=[])
# Immutable: Tuples, strings, numbers, True, False, None


def customer_list(iterable_clients, my_list=None):
    if my_list is None:
        my_list = []
    my_list.extend(iterable_clients)
    return my_list


my_list_client_1 = ['Fabrício']
client1 = customer_list(['João', 'Maria', 'Eduardo'], my_list_client_1)
client2 = customer_list(['Marcos', 'Jonas', 'Zico'])
client3 = customer_list(['José'])

print(client1)
print(client2)
print(client3)

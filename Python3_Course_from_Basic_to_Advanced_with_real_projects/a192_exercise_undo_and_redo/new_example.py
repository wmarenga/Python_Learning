from os import system
from time import sleep

my_list = []
undo = []
exception_list = ['List', 'list', 'Undo', 'undo', 'Redo', 'redo',
                  'Clear', 'clear', 'L', 'l', 'U', 'u', 'R', 'r', 'C', 'c']


def printgraphic(msg):
    print('='*50)
    print(msg)
    print('='*50)


def internal():
    print('='*50)
    print('Tarefas:')
    for index, item in enumerate(my_list):
        print(f' {index} -> {item}')


def to_execute(input):
    if input in exception_list:
        if input[0] == 'L':
            internal()
        elif input == 'U':
            if my_list:
                undo.append(my_list[-1])
                my_list.pop()
                internal()
            else:
                printgraphic('Nothing to undo.')
        elif input[0] == 'R':
            if undo:
                my_list.append(undo[-1])
                undo.pop()
                internal()
            else:
                printgraphic('Nothing to Redo.')
        elif input[0] == 'C':
            system('cls')
    else:
        my_list.append(input)
        internal()


while True:
    print('='*50)
    print('Commands: List[L], Undo[U], Redo[R], Clear[C] and Exit[E].')
    opt = input('Enter a command or task: ').capitalize()
    to_execute(opt)

    if opt[0] == 'E':
        system('cls')
        print('Shutting down...')
        sleep(3)
        break

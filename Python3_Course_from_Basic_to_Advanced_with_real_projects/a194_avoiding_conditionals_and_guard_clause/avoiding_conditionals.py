"""
Task list with undo and redo
Music to code =)
Everybody wants to rule the world - Tears for fears
todo = [] -> task list
todo = ['make coffee'] -> Add make coffee
todo = ['make coffee', 'walk'] -> Add walk
undo = ['make coffee',] -> Redo ['walk']
undo = [] -> Redo ['walk', 'make coffee']
redo = todo ['make coffee']
redo = todo ['make coffee', 'walk']
"""
import os


def to_list(tasks):
    print()
    if not tasks:
        print('No tasks to list', '\n')
        return

    print('Tasks:')
    for task in tasks:
        print(f'\t{task}')  # \t = tab
    print()


def to_undo(tasks, tasks_redo):
    print()
    if not tasks:
        print('No tasks to undo.')
        return

    task = tasks.pop()
    print(f'{task=} removed from to-do list.')
    tasks_redo.append(task)
    print()
    to_list(tasks)


def to_redo(tasks, tasks_redo):
    print()
    if not tasks_redo:
        print('No tasks to redo.')
        return

    task = tasks_redo.pop()
    print(f'{task=} added to the task list.')
    tasks.append(task)
    print()
    to_list(tasks)


def to_add(task, tasks):
    print()
    task = task.strip()
    if not task:
        print('You have not entered a task.')
        print(f'{task=} added to the task list.')
        return
    print(f'{task=} added to the task list.')
    tasks.append(task)
    print()
    to_list(tasks)


tasks = []
tasks_redo = []

while True:
    print('Commands: list, undo and redo')
    task = input('Enter a task or command: ')

    commands = {
        'list': lambda: to_list(tasks),
        'undo': lambda: to_undo(tasks, tasks_redo),
        'redo': lambda: to_redo(tasks, tasks_redo),
        'clear': lambda: os.system('cls'),
        'add': lambda: to_add(task, tasks),
    }
    commands = commands.get(task) if commands.get(task) is not None else \
        commands['add']
    commands()

    # if task == 'list':
    #     to_list(tasks)
    #     continue
    # elif task == 'undo':
    #     to_undo(tasks, tasks_redo)
    #     to_list(tasks)
    #     continue
    # elif task == 'redo':
    #     to_redo(tasks, tasks_redo)
    #     to_list(tasks)
    #     continue
    # elif task == 'clear':
    #     os.system('cls')
    #     continue
    # else:
    #     to_add(task, tasks)
    #     to_list(tasks)
    #     continue

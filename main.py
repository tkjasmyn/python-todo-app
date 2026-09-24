import os, json
from utils import add, view_tasks, complete_task, edit_task, delete_task, filter_tasks

if os.path.exists('tasks.json'):
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
else:
    tasks = []

while True:
    print('\n==== TODO Application ====')
    print('1. Add task\n2. View tasks\n3. Complete task\n4. Edit task\n5. Delete task\n6. Filter tasks\n7. Exit')

    user_input = input('> ').strip()
    if user_input == '1':
        add(tasks)
    elif user_input == '2':
        view_tasks(tasks)
    elif user_input == '3':
        complete_task(tasks)
    elif user_input == '4':
        edit_task(tasks)
    elif user_input == '5':
        delete_task(tasks)
    elif user_input == '6':
        filter_tasks(tasks)
    elif user_input == '7':
        print('\nGoodbye!')
        break
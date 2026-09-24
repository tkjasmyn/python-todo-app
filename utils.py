import json
from datetime import datetime

ID_WIDTH = 5
TASK_WIDTH = 12
STATUS_WIDTH = 10
PRIORITY_WIDTH = 10
DUE_WIDTH = 12
TIME_WIDTH = 12

def get_due_date():
    while True:
        date_choice = input('Enter due date (YYYY-MM-DD): ').strip()
        if date_choice == '':
            return 'None'

        try:
            date = datetime.strptime(date_choice, '%Y-%m-%d')
            return date.strftime('%Y-%m-%d')
        except ValueError:
            print('\nInvalid date, try again\n')

def add(tasks):
    task_name = input('Task Name: ').strip()

    if tasks:
        task_id = tasks[-1]['id'] + 1
    else:
        task_id = 1

    status = 'Pending'

    priority = 'None'

    due = get_due_date()

    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')

    task = {
        'id': task_id,
        'task': task_name,
        'status': status,
        'priority': priority,
        'due': due,
        'time': current_time
    }
    tasks.append(task)
    print('Task added successfully')

    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def view_tasks(tasks):
    if not tasks:
        print('Tasks list is empty')
        return

    print(f"\n{'ID':<{ID_WIDTH}} {'Task':<{TASK_WIDTH}} {'Status':<{STATUS_WIDTH}} {'Priority':<{PRIORITY_WIDTH}} {'Due':<{DUE_WIDTH}} {'Time':<{TIME_WIDTH}}")

    for task in tasks:
        Id = task['id']
        Task = task['task']
        Status = task['status']
        Priority = task['priority']
        Due = task.get('due', 'None')
        Time = task['time']

        print(f"{Id:<{ID_WIDTH}} {Task:<{TASK_WIDTH}} {Status:<{STATUS_WIDTH}} {Priority:<{PRIORITY_WIDTH}} {Due:<{DUE_WIDTH}} {Time:<{TIME_WIDTH}}")

def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return
    
    user_input = input('\nEnter task id: ').strip()

    try:
        target_id = int(user_input)
    except ValueError:
        print('Invalid ID')
        return

    for task in tasks:
        if target_id == task['id']:
            task['status'] = 'Done'
            with open('tasks.json', 'w') as file:
                json.dump(tasks, file, indent=4)
            print('Task marked done')
            break
    else:
        print('Task not found')

def edit_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    user_input_id = input('\nEnter id of task you want to edit: ').strip()

    try:
        target_id = int(user_input_id)
    except ValueError:
        print('Invalid ID')
        return

    for task in tasks:
        if target_id == task['id']:
            print('\nWhat do you want to edit:\n1. Name\n2. Priority\n3. Due date')
            user_input_edit = input('> ').strip()
            if user_input_edit == '1':
                task_name = input('Task Name: ').strip()
                task['task'] = task_name
            elif user_input_edit == '2':
                priority_map = {'1': 'High', '2': 'Medium', '3': 'Low'}
                while True:
                    print('\nSet priority:\n1. High\n2. Medium\n3. Low')
                    task_priority = input('> ').strip()

                    if task_priority not in priority_map:
                        print('\nInvalid option')
                        continue
                    wanted = priority_map[task_priority]
                    task['priority'] = wanted
                    print(f'\nPriority set to {wanted}')
                    break
            elif user_input_edit == '3':
                task['due'] = get_due_date()
            else:
                print('\nInvalid edit option')
                return
                        
            now = datetime.now()
            task['time'] = now.strftime('%H:%M:%S')
            with open('tasks.json', 'w') as file:
                json.dump(tasks, file, indent=4)
            print('Task edited successfully')
            break
    else:
        print('\nTask not found')

def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return
    
    user_input = input('\nEnter task id: ').strip()

    try:
        target_id = int(user_input)
    except ValueError:
        print('\nInvalid ID')
        return

    for index, task in enumerate(tasks):
        if target_id == task['id']:
            del tasks[index]
            with open('tasks.json', 'w') as file:
                json.dump(tasks, file, indent=4)
            print('\nTask deleted')
            break
    else:
        print('\nTask not found')

def filter_tasks(tasks):
    print('\n1. By priority\n2. By status')
    filter_choice = input('> ').strip()
    if filter_choice == '1':
        priority_map = {'1': 'High', '2': 'Medium', '3': 'Low', '4': 'None'}
        priority_matches = []

        print('\n1. High\n2. Medium\n3. Low\n4. None')
        priority_choice = input('> ').strip()

        if priority_choice not in priority_map:
            print('\nInvalid option')
            return

        priority_wanted = priority_map[priority_choice]

        for task in tasks:
            if task['priority'] == priority_wanted:
                priority_matches.append(task)

        if priority_matches:
            view_tasks(priority_matches)
        else:
            print(f'\nNo {priority_wanted} priority task found')
    elif filter_choice == '2':
        status_map = {'1': 'Done', '2': 'Pending'}
        status_matches = []

        print('\n1. Done\n2. Pending')
        status_choice = input('> ').strip()

        if status_choice not in status_map:
            print('\nInvalid option')
            return

        status_wanted = status_map[status_choice]

        for task in tasks:
            if task['status'] == status_wanted:
                status_matches.append(task)
        if status_matches:
            view_tasks(status_matches)
        else:
            print(f'\nNo {status_wanted} task found')
    else:
        print('\nInvalid option')

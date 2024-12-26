import datetime

print("Good Day, Welcome to TO-DO List Application")

def existing_edit():
    created_file = input('What is the name.(Please also indicate what it saved at e.g data.csv/data.pdf/data.txt): ')
    add = input('Do you want to add a to-do list? Please type yes or no: ')
    if add == 'yes':
        day = datetime.datetime.now()
        task = input('Task number: ')
        ToDo = input('TO-DO: ')
        default_name = 'Not_Done'
        default = '❌'
        TO_DO = {
            'Day': day.strftime("%x"),
            'To_do': ToDo,
            f'Task_{task}_{default_name}': default
        }

        # Save and Load Functions: Save the tasks to a file so that the data persists between program runs.
        for key, value in TO_DO.items():
            f = open(created_file, 'a')
            f.write(str(f'{key}: {value}\n'))

        space = open(created_file, 'a')
        space.write('\n----------------------------------\n')
    else:
    # View Tasks Function: Display a list of all tasks with their statuses.
        view = open(created_file, 'r')
        print(view.read())

    if add == 'no':
        pass
    else:
        view = open(created_file, 'r')
        print(view.read())


    # Edit a Task Function: Allow the user to edit an existing task's title or change its status.
    edit_data = input('Do you want to edit data, please type yes or no: ')
    if edit_data == 'yes':
        with open(created_file, 'r') as file:
            lines = file.readlines()

        name = input("What is the name of the data that you want to change: ")
        value = input('What is the value inside the data: ')
        data = input('What data do you want to replace with: ')

        for x, line in enumerate(lines):
            if line.startswith(f'{name}: {value}'):
                field = line.strip().split('/')
                field[0] = f"{name}: {data}"
                lines[x] = f"{name}: {data}".join(field) + '\n'

        with open(created_file, 'w') as file:
            file.writelines(lines)
    else:
        print('No edit has been made!')

    # Mark Task as Completed Function: Allow the user to mark a task as completed.
    Completed_task = input("Did you complete a task, Please type yes or no: ")
    if Completed_task == 'yes':
        with open(created_file, 'r') as file:
            lines = file.readlines()

        task_number = input("Which task did you Complete, Please type in the number: ")

        for x, line in enumerate(lines):
            if line.startswith(f'Task_{task_number}_Not_Done: ❌'):
                field = line.strip().split('/')
                field[0] = f'Task_{task_number}_Done: ✅'
                lines[x] = f'Task_{task_number}_Done: ✅'.join(field) + '\n'

        with open(created_file, 'w') as file:
            file.writelines(lines)
    else:
        print('The are no task completed.')

start = input('Do you want to make a To_do list? Please type in yes or no: ')

while start == 'yes':
    existing_file = input('Do you have an existing file?(Please note: if the file has already have data on it, it going to be overwrite!) ')
    if existing_file == 'yes':
        existing_edit()
        print('Data have been edited, have a nice day 😊.')
        break
    else:
        file_name = input('What well be the name of the file you want to save the data: ')
        with open(file_name, 'a') as load:
            load.write('list: ')

    # Add a Task Function: Prompt the user to enter the title of a task.
    add = input('Do you want to add a to-do list? Please type yes or no: ')
    if add == 'yes':
        day = datetime.datetime.now()
        task = input('Task number: ')
        ToDo = input('TO-DO: ')
        default_name = 'Not_Done'
        default = '❌'
        TO_DO = {
            'Day': day.strftime("%x"),
            'To_do': ToDo,
            f'Task_{task}_{default_name}': default
        }

        # Save and Load Functions: Save the tasks to a file so that the data persists between program runs.
        for key, value in TO_DO.items():
            f = open(file_name, 'a')
            f.write(str(f'{key}: {value}\n'))

        space = open(file_name, 'a')
        space.write('\n----------------------------------\n')
    else:
    # View Tasks Function: Display a list of all tasks with their statuses.
        view = open(file_name, 'r')
        print(view.read())

    if add == 'no':
        pass
    else:
        view = open(file_name, 'r')
        print(view.read())


    # Edit a Task Function: Allow the user to edit an existing task's title or change its status.
    edit_data = input('Do you want to edit data, please type yes or no: ')
    if edit_data == 'yes':
        with open(file_name, 'r') as file:
            lines = file.readlines()

        name = input("What is the name of the data that you want to change: ")
        value = input('What is the value inside the data: ')
        data = input('What data do you want to replace with: ')

        for x, line in enumerate(lines):
            if line.startswith(f'{name}: {value}'):
                field = line.strip().split('/')
                field[0] = f"{name}: {data}"
                lines[x] = f"{name}: {data}".join(field) + '\n'

        with open(file_name, 'w') as file:
            file.writelines(lines)
    else:
        print('No edit has been made!')

    # Mark Task as Completed Function: Allow the user to mark a task as completed.
    Completed_task = input("Did you complete a task, Please type yes or no: ")
    if Completed_task == 'yes':
        with open(file_name, 'r') as file:
            lines = file.readlines()

        task_number = input("Which task did you Complete, Please type in the number: ")

        for x, line in enumerate(lines):
            if line.startswith(f'Task_{task_number}_Not_Done: ❌'):
                field = line.strip().split('/')
                field[0] = f'Task_{task_number}_Done: ✅'
                lines[x] = f'Task_{task_number}_Done: ✅'.join(field) + '\n'

        with open(file_name, 'w') as file:
            file.writelines(lines)
    else:
        print('The are no task completed.')

    start = input('Do you still want to make a To_do list? Please type in yes or no: ')
    if start == 'no':
        break
else:
    print('bye')
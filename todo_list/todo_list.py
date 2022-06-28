intro = '''
  _____         _
 |_   _|__   __| | ___  ___
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
'''

help = '''
TODO LIST HELP
Type 'q' to quit
To add a todo to the list, type it and hit enter
To complete a todo enter its number
'''

print(intro)

todo_list = []
completed_list = []
while True:
    for i in range(len(todo_list)):
        print(f'{i+1}) {todo_list[i]}')
    print('*'*50)
    print("Enter a command. Type 'h' for help: ")
    command = input('>')
    if command == 'q' or command == 'quit':
        break
    elif command == 'h':
        print(help)
    elif command.isnumeric():
        index = int(command)-1
        if index >= len(todo_list):
            print('='*50)
            print('*'*50)
            print('There is no todo with that number')
            print('*'*50)
            print('='*50)
        else:
            removed = todo_list.pop(index)
            completed_list.append(removed)
    else:
        todo_list.append(command)
if completed_list:
    print(f'You completed{len(completed_list)} todo(s) today')
    for completed_todo in completed_list:
        print(f"* {completed_todo}")
print('Good Bye')

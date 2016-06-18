list_of_numbers = []
no_of_commands = int(input("enter no.of commands : "))
commands = []
for i in range(no_of_commands):
    command = input()
    commands.append(command)

for cmd_line in commands:
    split_command = cmd_line.split()
    command = split_command[0]
    if command == "insert":
        '''do insert'''
        i = int(split_command[1])
        x = int(split_command[2])
        list_of_numbers.insert(i, x)

    elif command == "append":
        '''do append'''
        x = int(split_command[1])
        list_of_numbers.append(x)
    elif command == "pop":
        '''do pop'''
        list_of_numbers.pop()
    elif command == "print":
        '''do print'''
        print(list_of_numbers)
    elif command == "remove":
        '''do remove'''
        x = int(split_command[1])
        list_of_numbers.remove(x)
    elif command == "sort":
        '''do sort'''
        list_of_numbers.sort()
    elif command == "reverse":
        '''do reverse'''
        list_of_numbers.reverse()

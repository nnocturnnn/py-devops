import sqlite3

def close(command, connections):
    command_arg = command.split()
    if len(command_arg) < 2:
        print("command 'close' not given database filename")
    elif len(command_arg) > 2:
        print("command 'close' given too many arguments")
    else:
        if command_arg[1] in connections:
            try:
                connections[command_arg[1]].close()
                connections.pop(command_arg[1],None)
                print(f'Closed connection to database "{command_arg[1]}"')
            except Exception as exc:
                print(exc)
        else:
            print(f'Cannot close connection to "{command_arg[1]}". Not connected.')

def execute(command, connections):
    commandDB_exe = command.split(' "')
    command_arg = commandDB_exe[0].split()
    if commandDB_exe[1][-1] == '"':
        try:
            connections[command_arg[1]].execute(commandDB_exe[1][0:-1])
            print("Executed SQL statement.")
        except Exception as exc:
            print(exc)
    else:
        print("SQL statement must have double quotes on both sides")

def connect(command, connections):
    command_arg = command.split()
    if len(command_arg) < 2:
        print("command 'connect' not given database filename")
    elif len(command_arg) > 2:
        print("command 'connect' given too many arguments")
    else:
        if command_arg[1] in connections:
            print(f'Already connected to database "{command_arg[1]}".')
        else:
            try:
                connections.update({command_arg[1] : sqlite3.connect(command_arg[1])})
                print(f'Created connection to database "{command_arg[1]}".')
            except Exception as exc:
                print(exc)

def helps(command):
    command_arg = command.split()
    if len(command_arg) < 2:
        print('Available commands:\n- help\n- connect [database]\n\
- close [database]\n- execute [database] "[SQL statement]"\n- show\n- exit')
    else:
        print("command 'help' given too many arguments.")

def show(command, connections):
    command_arg = command.split()
    if len(command_arg) < 2:
        if len(connections) == 0:
            print('No connections.')
        else:
            print("Connected to:")
            print(list(connections.keys()))
    else:
        print("command 'show' given too many arguments.")

def exit_f(command, connections):
    command_arg = command.split()
    if len(command_arg) < 2:
        if len(connections) > 0:
            for i in connections:
                connections[i].close()
                print(f'Closed connection to database "{i}".')
        exit()
    else:
        print("command 'exit' given too many arguments.")

def loop():
    connections = {}
    while True:
        command = input("Enter command: ")
        if command.startswith("help"):
            helps(command)
        elif command.startswith("show"):
            show(command, connections)
        elif command.startswith("exit"):
            exit_f(command, connections)
        elif command.startswith("connect"):
            connect(command, connections)
        elif command.startswith("close"):
            close(command, connections)
        elif command.startswith("execute"):
            execute(command, connections)
        else:
            print('Invalid command. Try "help" to see available commands.')


loop()
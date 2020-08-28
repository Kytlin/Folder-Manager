import os
from RunCommand import runCommand

path = ''
while True:
    path = input("Please provide a path: ")
    if (os.path.exists(path)):
        os.chdir(path)
        break
    elif (path == "exit"):
        break
    else:
        print("Invalid path (please include \"C:/\" at the beginning of your path).")

if (os.path.exists(path)):
    command = input("\nWelcome to the Folder Manager Application. Type \"help\" to list commands and \"path\" to change file path.\n")
    commandList = ['\i', '\d', '\m', '\l', '\-r']

    while True: 
        print(" > ", end='')
        command = str(input())
        if (command == "help"):
            print('''
            +----------------------------------------------------------------------------+
            | Commands...                                                                |
            |                                                                            |
            | \i [name] : add file/folder in current directory                           |
            | \i [dir/file] [dir] : add file/folder in other directory                   |
            | \d [name]: delete file/folder in current directory                         |
            | \d [dir/file] [dir] : delete file/folder in other directory                |
            | \m [dir/file] [dir] : move file from one directory to another              |
            | \-r [initName] [finalName] : rename file/folder                            | 
            | \l [file]: print out the path of the file                                  |
            | exit : exit out of program                                                 |
            +----------------------------------------------------------------------------+
            ''')
        elif (command == "change"):
            path = input("Path: ")
            os.chdir(path)
        elif (command == "exit"):
            break
        elif (command.split()[0] in commandList):
            runCommand(command, path)
        else:
            print("Invalid entry.")

        command = str(input())
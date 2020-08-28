import os

def listPath (command, path):
    if (len(command.split()) == 1):
        print("Not enough arguments provided.")

    elif (len(command.split()) == 2):
        fullPath = ""

        # Find path of file
        for dirpath, dirnames, filenames in os.walk(path):
            if (command.split()[1] in filenames):
                fullPath = dirpath
                break
        
        print(f"\"{command.split()[1]}\" is in path: ", fullPath)

    else:
        print("Too many arguments provided.")
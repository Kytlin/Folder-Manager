import os

def rename(command, path):
    if (len(command.split()) == 2):
        print("Not enough arguments provided.")

    elif (len(command.split()) == 3):
        fullPath = ""

        # Find path of file / folder
        for dirpath, dirnames, filenames in os.walk(path):
            if (command.split()[1] in filenames or dirnames):
                fullPath = dirpath
                break

        # Set directory to path found
        os.chdir(fullPath)
        os.rename(command.split()[1], command.split()[2])

    else:
        print("Too many arguments provided.")
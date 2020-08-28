import os

def make(command, path):

    if (len(command.split()) == 1):
        print("Not enough arguments provided.")

    elif (len(command.split()) == 2):
        # Adding file in current directory (\i [file])
        if ('.' in command.split()[1]):
            filePath = os.path.join(path, command.split()[1])
            with open(filePath, 'w') as f:
                f.write("")

        # Adding folder in current directory (\i [dir])
        else:
            os.mkdir(command.split()[1])

    elif (len(command.split()) == 3): 
        # Adding file in another directory (\i [dir] [file])
        if ('.' in command.split()[1] and not '.' in command.split()[2]):
            for dirpath, dirnames, filenames in os.walk(path):
                if (command.split()[2] in dirnames):
                    filePath = os.path.join(dirpath, command.split()[2])
                    print(filePath)
                    break

            filePath = os.path.join(filePath, command.split()[1])
            with open(filePath, 'w') as f:
                f.write("")

        # Adding folder in another directory (\i [dir] [dir])
        elif (not '.' in command.split()[1] and command.split()[2]):
            for dirpath, dirnames, filenames in os.walk(path):
                if (command.split()[2] in dirnames):
                    folderPath = os.path.join(folderPath, command.split()[2])
                    break

            os.chdir(folderPath)
            os.mkdir(command.split()[2])

        else:
            print("Second argument cannot be a file.")

    else:
        print("Too many arguments provided.")
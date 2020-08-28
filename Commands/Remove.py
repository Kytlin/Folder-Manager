import os

def remove(command, path):
    if (len(command.split()) == 1):
        print("Not enough arguments provided.")

    elif (len(command.split()) == 2):
        # Deleting file in current directory (\d [file])
        if ('.' in command.split()[1]):
            if (len(command.split()) == 2):
                os.remove(command.split()[1])

        # Deleting folder in current directory (\d [dir])
        else:
            os.rmdir(command.split()[1])

    elif (len(command.split()) == 3): 
        # Deleting file in another directory (\d [dir] [file])
        if ('.' in command.split()[1] and not '.' in command.split()[2]):
            for dirpath, dirnames, filenames in os.walk(path):
                if (command.split()[2] in dirnames):
                    filePath = os.path.join(dirpath, command.split()[2])
                    break
                
            os.chdir(filePath)
            os.remove(command.split()[1])

        # Deleting folder in another directory (\d [dir] [dir])
        elif (not '.' in command.split()[1] and command.split()[2]):
            for dirpath, dirnames, filenames in os.walk(path):
                if (command.split()[2] in dirnames):
                    folderPath = os.path.join(folderPath, command.split()[2])
                    break

            os.chdir(folderPath)
            os.rmdir(command.split()[2])

        else:
            print("Second argument cannot be a file.")

    else:
        print("Too many arguments provided.")
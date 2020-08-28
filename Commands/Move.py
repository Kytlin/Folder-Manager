import os
import shutil

def move(command, path):
    foundInit = False
    foundLoc = False
    locPath = ""

    if (len(command.split()) < 3):
        print("Not enough arguments provided.")

    elif ('.' in command.split()[1] and not '.' in command.split()[2]):
        # Move file / folder into a directory (\m [dir/file] [dir])
        for dirpath, dirnames, filenames in os.walk(path):
            if (foundInit and foundLoc):
                break

            # Find path of the location directory 
            if (command.split()[2] in dirnames):
                locPath = os.path.join(dirpath, command.split()[2])
                foundInit = True
            # Find path of the file
            elif (command.split()[1] in filenames):
                initPath = os.path.join(dirpath, command.split()[1])
                foundLoc = True

        locPath = os.path.join(locPath, command.split()[1])
        shutil.move(initPath, locPath)
    
    elif (not '.' in command.split()[1] and command.split()[2]):
        # Move file / folder into a directory (\m [dir/file] [dir])
        for dirpath, dirnames, filenames in os.walk(path):
            if (foundInit and foundLoc):
                break

            # Find path of the location directory 
            if (command.split()[2] in dirnames):
                locPath = os.path.join(dirpath, command.split()[2])
                foundInit = True
            # Find path of the folder
            elif (command.split()[1] in dirnames):
                initPath = os.path.join(dirpath, command.split()[1])
                foundLoc = True

        locPath = os.path.join(locPath, command.split()[1])
        shutil.move(initPath, locPath)

    elif ('.' in command.split()[2]):
        print("Second Argument cannot be a file.")

    else:
        print("Too many arguments provided.")
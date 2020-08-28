import os
from Commands.ListPath import listPath
from Commands.Make import make
from Commands.Remove import remove
from Commands.Move import move
from Commands.Rename import rename

def runCommand(command, path):
    run = {
        '\l': listPath,
        '\i': make,
        '\d': remove,
        '\m': move,
        '\-r': rename
    }
    run[command.split()[0]](command, path)
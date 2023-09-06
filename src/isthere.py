#importing libs
import os
import sys

# Just Init for a color pallet
ANSI_COLOR_RED = "\x1b[31m"
ANSI_COLOR_GREEN = "\x1b[32m"
ANSI_COLOR_YELLOW = "\x1b[33m"
ANSI_COLOR_BLUE = "\x1b[34m"
ANSI_COLOR_MAGENTA = "\x1b[35m"
ANSI_COLOR_CYAN = "\x1b[36m"
ANSI_COLOR_RESET = "\x1b[0m"

# Adding Args to a variable
filepath = sys.argv[1]

# Checking if file exists
check = os.path.exists(filepath)

# Some basic error handling
if check == False:
    check2 = os.path.isfile(filepath)
    if check2 == False:
        print (ANSI_COLOR_RED + "Either the file/path doesnt exist or the program doesnt have the permission to read it" + ANSI_COLOR_RESET)
        fail = True
    if check2 == True:
        print (ANSI_COLOR_CYAN + "The file/folder: " + ANSI_COLOR_RESET + ANSI_COLOR_GREEN + filepath + ANSI_COLOR_RESET + ANSI_COLOR_CYAN + " exists :)" + ANSI_COLOR_RESET)
if check == True:
    print (ANSI_COLOR_CYAN + "The file/folder: " + ANSI_COLOR_RESET + ANSI_COLOR_GREEN + filepath + ANSI_COLOR_RESET + ANSI_COLOR_CYAN + " exists :)" + ANSI_COLOR_RESET)


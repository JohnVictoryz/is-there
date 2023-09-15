#importing libs
import os
import sys
import platform

# Just Init for a color pallet
ANSI_COLOR_RED = "\x1b[31m"
ANSI_COLOR_GREEN = "\x1b[32m"
ANSI_COLOR_YELLOW = "\x1b[33m"
ANSI_COLOR_BLUE = "\x1b[34m"
ANSI_COLOR_MAGENTA = "\x1b[35m"
ANSI_COLOR_CYAN = "\x1b[36m"
ANSI_COLOR_RESET = "\x1b[0m"

# Init of nopar and os variable
nopar = False
os = platform.system()
# Basic Error Handling
try:
    filepathchk = sys.argv[1]
except IndexError:
    print(ANSI_COLOR_RED + "You didn't specify a file or directory\n" + ANSI_COLOR_RESET + """isthere <filepath> <args>
          -H or -h or --help Help with this tool
          -Ad Automatically create a directory if the directory doesn't exist
          -Af Automatically create a file if the file doesn't exist
          -Md Manually create a directory if the directory doesn't exist 
          -Mf Manually create a file if the file doesn't exist
          -M Manually create a file or directory if it doesn't exist
          """)
    exit()
try:
    par = sys.argv[2]
except IndexError:
    nopar = True

#Checking if file exists
if filepathchk == "-H" or filepathchk == "-h" or filepathchk == "--help" or filepathchk == "help":
    print("""isthere <filepath> <args>
          -H or -h or --help Help with this tool
          -Ad Automatically create a directory if the directory doesn't exist
          -Af Automatically create a file if the file doesn't exist
          -Md Manually create a directory if the directory doesn't exist 
          -Mf Manually create a file if the file doesn't exist
          -M Manually create a file or directory if it doesn't exist
          """)
check = os.path.exists(filepathchk)

# Some basic error handling
if check == False:
    check2 = os.path.isfile(filepathchk)
    failchk1 = True
    if check2 == False:
        print (ANSI_COLOR_RED + "Either the file/path doesnt exist or the program doesnt have the permission to read it" + ANSI_COLOR_RESET)
        failchk2 = True
    if check2 == True:
        print (ANSI_COLOR_CYAN + "The file/folder: " + ANSI_COLOR_RESET + ANSI_COLOR_GREEN + filepath + ANSI_COLOR_RESET + ANSI_COLOR_CYAN + " exists :)" + ANSI_COLOR_RESET)
if check == True:
    print (ANSI_COLOR_CYAN + "The file/folder: " + ANSI_COLOR_RESET + ANSI_COLOR_GREEN + filepath + ANSI_COLOR_RESET + ANSI_COLOR_CYAN + " exists :)" + ANSI_COLOR_RESET)


if failchk1 == True and nopar != True or failchk2 == True and nopar != True:
    if par == "-M":
        filetype = input("Do you want a file or a folder type fd for folder or fl for file: ")
        if filetype == "fd":
            path = input("Nice! Now where you want your folder (A.K.A the path (ALSO TYPE THE LAST / OR \ )): ")
            cmd = "mkdir " + path
            os.system(cmd)
            print(ANSI_COLOR_CYAN + "Folder Created ;)" + ANSI_COLOR_RESET)
        filename = input("Nice! Now type the filename including the extension if you want: ")
        path = input("Almost There. Now type where do you want the file (A.K.A The path (ALSO TYPE THE LAST / OR \ )): ")
        if os == 'Linux' or os == 'Darwin':
            cmd = "touch " + path + filename
            os.system(cmd)
            print(ANSI_COLOR_CYAN + "File Created ;)" + ANSI_COLOR_RESET)
        if os == 'Windows':
            cmd = "type nul >> " + path + filename
            os.system(cmd)
            print(ANSI_COLOR_CYAN + "File Created ;)" + ANSI_COLOR_RESET)
    if par == "-Md":
        foldername = input("Type the name of the folder: ")
        path = input("Almost There. Now type where do you want your folder (A.K.A The path (ALSO TYPE THE LAST / OR \ )): ")
        cmd = "mkdir " + path + foldername
        os.system(cmd)
        print(ANSI_COLOR_CYAN + "Folder Created ;)" + ANSI_COLOR_RESET)
    if par == "-Mf":
        filename = input("Type the filename including the extension if you want: ")
        path = input("Almost There. Now type where do you want you file (A.K.A The path (ALSO TYPE THE LAST / OR \ )): ")
        if os == 'Linux' or os == 'Darwin':
            cmd = "touch " + path + filename
            os.system(cmd)
            print(ANSI_COLOR_CYAN + "File Created ;)" + ANSI_COLOR_RESET)
        if os == 'Windows':
            cmd = "type nul >> " + path + filename
            os.system(cmd)
            print(ANSI_COLOR_CYAN + "File Created ;)" + ANSI_COLOR_RESET)
    if par == "-Ad":
        cmd "mkdir " + filepathchk
        os.system(cmd)
    if par == "-Af":
        if os == 'Linux' or os == 'Darwin':
            cmd = "touch " + filepathchk
        if os == 'Windows':
            cmd = "type nul >> " + filepathchk
            os.system(cmd)
    else:
        print(ANSI_COLOR_RED + "Invalid Parameter :(" + ANSI_COLOR_RESET)
        exit()


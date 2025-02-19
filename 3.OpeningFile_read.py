#Opening a file
'''
open()
f = open(filename, mode="r", buffering, encoding = "None", errors = None, newline = None, closefd = True)
important one are filename , mode , encoding
'''
#f = open(filename, mode = "r")
"""
filename = file to be access // directory can be used
mode = access mode(purpose of opening file)
f = file handler, file pointer
"""

#f points at the beginning of the file
'''
filename is always string
r/w is always string
'''

#Example
'''
create a text file in an folder , in my case its in the folder within which the code is saved.
'''
f = open("files/3rd video.txt")
#by default mode is for read i.e. mode="r"
#directory from current directory to file directory is written here
if f:
    print("file successfully open")
# This code won't run directly in IDLE
# now we will go to cmd
"""
change directory using "cd" command
then open this code using "python codename.py"
"""

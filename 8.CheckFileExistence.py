#Check File Exist or not

#f = open("files/3rd video.txt")
#if file don't exist code gives error

#OS module
"""
isfile() function/method  returns boolean value

this function exist in os module's submodule path module

os.path.isfile()
"""
#Code

import os.path as p
if p.isfile("files/3rd video.txt"):
    print("File exists !!! Opening the file ...")
    f = open("files/3rd video.txt")
    if f:
        print("File opened")
    f.close()
else:
    print("File doesn't exist")

    
#Alternate
"""
import os
if os.path.isfile("files/3rd video.txt"):
    print("File exists !!! Opening the file ...")
    f = open("files/3rd video.txt")
    if f:
        print("File opened")
    f.close()
else:
    print("File doesn't exist")
"""

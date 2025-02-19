#File Object Methods
"""
readable() - Checks if the file is readable or not. //Returns boolean value
writable() - Checks if the file is writable or not. //Returns boolean value

We set the mode to "r" or "w".
"""
f = open("files/3rd video.txt","r")
if f:
    print("File opened")
    f = open("files/3rd video.txt","r")
    print("The is file is readable ?",f.readable())
    print("The is file is writable ?",f.writable())
f.close()
if f.closed:
    print("File closed")

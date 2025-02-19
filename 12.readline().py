# readline()
"""
This function is used to read a single line from the file.
"""
# File_object.readline(size) //cursor position 0 at start //size = only read that no.characters from that line
# Keep the moving of cursor in mind. It moves cursor by cursor.
# Code
f = open("files/3rd video.txt")
data = f.readline(3)
data1 = f.readline(2)
print(data)
print(data1)
f.close()

# Output
"""
Hello World

hello user
"""
# Gap is because of the \n from end of sentence in txt file and default end="\n" for print()
#code without size argument
f = open("files/3rd video.txt")
data = f.readline()
data1 = f.readline()
print(data)
print(data1)
f.close()

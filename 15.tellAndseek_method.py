#tell()
#seek()
#need to know cursor concept
"""
initially cursor is at 0 , after reading cursor moves.
if you read 3 character , it will move 3 step forward. with operations , cursor keeps movinf ahead.
"""
#tell()
"""
used to find current position of the cursor/file pointer.
TELLS THE POSITION OF CURSOR FROM THE BEGINNING. AND IN BEGINNING ITS 0. 

similar to indexing in string. position starts from 0.
"""
#code
print("using tell()")
f = open("files/3rd video.txt","r")
data = f.tell() #it doesn't print , but returns a value.
print(data)
print(f.read(3))
print(f.tell())

#now reading whole remaining file
print(f.read())
print(f.tell())
f.closed

#******************************************************************************************************
#seek()
"""
used to change the position of cursor/file pointer.
POSITION ALWAYS COUNTED FROM THE BEGINNING i.e. 0
"""
#code
print("\n\nusing seek()")
f = open("files/3rd video.txt","r")
print(f.tell())
print(f.read(3))
print(f.tell())
f.seek(0)
print(f.tell())
print(f.read(3))
f.closed


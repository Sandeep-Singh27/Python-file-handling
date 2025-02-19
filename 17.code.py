#writing two lines in one arguemnt using \n
"""
f = open("files/3rd video.txt",mode="w")
if f:
    print("file opened")
print(f.tell())
f.write("hello world\njai mata di")
print(f.tell())
f.close()
"""
#trying to reopen and write to check overwriting
"""
f = open("files/3rd video.txt",mode="w")
if f:
    print("file opened")
print(f.tell())
f.write("hello world")
print(f.tell())
f.close()
"""
#writing twice
f = open("files/3rd video.txt",mode="w")
if f:
    print("file opened")
print(f.tell())
n = f.write("hello world")#here it will write in file + write() returns no. of character written in text file

# n = 11 since "hello world" has 11 character including " "

f.write("\njai mata di") #in this case cursor starts from current location and not beginning
print(f.tell())
f.close()

#reading the file
f = open("files/3rd video.txt",mode="r")
if f:
    print("file opened")
print(f.read())
f.close()

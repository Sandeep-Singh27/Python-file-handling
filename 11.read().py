#Reading the data from file:-
"""
read()
readline()
readline()
"""
#read()
"""
read data/content from a file and return as string in text mode.
returns bytes in binary mode.

f.read(size)
size is a optional . size : number of characters to be read.
there is no size argument in binary mode

negative or no size results in reading all the character

size occupies "\n, ,\r" like terms also.
"""
#Code
f=open("files/3rd video.txt")
data=f.read(10)
data1=f.read(5)
print(data)
print(data1)

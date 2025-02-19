#readlines()
"""
read all lines from a file and returns a list of lines.
"""
#file_object.readlines()

f = open("files/3rd video.txt","r")
data = f.readlines()
print(data)
f.close()
print(f.closed)

for i in data:
    print(i,end="") #print(i) will give one line gap because there would be \n\n.


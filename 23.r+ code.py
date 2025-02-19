f = open("files/3rd video.txt",mode='r+')
if f:
    print(f.name,"opened")
print("cursor is at",f.tell())
data = f.read()
print(data)
print("cursor is at",f.tell())
f.write("\nWriting new line using r+")
f.seek(0)
data1 = f.read()
print(data1)
f.close()

#read and write sequence doesn't really matter , just keep the cursor position in mid
#after performing operations like read and write.

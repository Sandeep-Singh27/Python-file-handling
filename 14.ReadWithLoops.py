f = open("files/3rd video.txt",mode="r",encoding="utf-8")
print(list(f))
#this will return lines as element of file , similar as readlines()
f.close()

#reopen file otherwise cursor is at the end of file
f = open("files/3rd video.txt",mode="r",encoding="utf-8")
data = f.readlines()
print(data)
f.close()

#using for loop
f = open("files/3rd video.txt",mode="r",encoding="utf-8")
for i in f:
    print(i,end="")
f.close()

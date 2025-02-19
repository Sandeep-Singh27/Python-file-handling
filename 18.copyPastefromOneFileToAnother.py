f = open("files/3rd video.txt","r")
if f:
    print(f.name,"opened")
data=f.readlines()
f.close()

f = open("files/18th video.txt","w")
if f:
    print(f.name,"opened")
for i in data:
    f.write(i)
f.close

f = open("files/18th video.txt","r")
if f:
    print(f.name,"opened")
data = f.read()#for size = 11 it prints "hello world" but for 13 it prints "hello world\nj"
print(data)
f.close

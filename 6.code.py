f = open("files/3rd video.txt",mode="r",encoding="utf-8")
if f:
    print("File Successfully opened")
print("File name is ",f.name)
print("File encoding is ",f.encoding)
print("File mode is ",f.mode)

if f.closed:
    print("File closed")
else:
    print("File not closed" )

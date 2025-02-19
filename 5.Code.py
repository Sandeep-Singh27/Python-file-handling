f = open("files/3rd video.txt","r")
if f:
    print("File successfully opened")
f.close()
if f.closed: #f.closed = True after the file is closed
#                         f.closed() is wrong            f.closed is right
    print("File successfully closed")
else:
    print("File not closed")

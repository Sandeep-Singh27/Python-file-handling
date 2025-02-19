f = open("files/3rd video.txt",mode="w+")
f.write("Using w+ on the file")
f.seek(0)
data = f.read()
print(data)
f.close()
#since file got truncate
"""
cursor 0 at start
file was empy since(truncate)
then wrote
cursor was at end , so to read the content we used seek to move cursor again to start position
then read the file
"""

#there can be dataloss in "w"

#mode="x" ,Gives FileExistError if file already exists
"""
important mode when we write data in file
prevents data loss
"""

#"x" writes only in a new file
#f = open("files/3rd video.txt","x") // FileExistsError: [Errno 17] File exists: 'files/3rd video.txt'
f = open("files/20th video.txt","x")
if f:
    print("file opened")
f.write("Hallo Moto\n")
f.close()


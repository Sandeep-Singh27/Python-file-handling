#In python object is considered in a boolean context of ,
#Truthliness and falsiness // spellings might be wrong but you know what i mean.
#existing objects are turthful
#empty objects (non-existing for custom objects) are false

f = open("files/3rd video.txt",mode = "r", buffering = 10)#utf-8 is an universal encoder ,window default = cp1252
#f = open("files/3rd video.txt",mode = "r", buffering = 10 , encoding = "utf-8")
if f:
    print("Opened")
print(f)

"""
f = open("files/3rd video.txt",mode = "r", buffering = 10) // key word arguments , order not compulsory
f = open("files/3rd video.txt","r", 10) //positional arguments , order compulsory
"""

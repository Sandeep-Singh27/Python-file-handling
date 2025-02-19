#count number of characters,words and line in a text file
f = open("files/3rd video.txt","r")
c = 0
w = 0
l = 0
for i in f:
    print(i,end="")
    l += 1
    i = i.strip()
    w += len(i.split(" "))
    i = i.replace(" ","")
    c += len(i)
print("\n",c,sep="")
print(w)
print(l)
f.close()

"""PROBLEM"""
# string.strip() only works at start and ending of the string . default removes spaces , tabs and newline.

"""IMPORTANT"""
# string.replace("to_be_replaced","replaced_by") might come helpful.
    
    

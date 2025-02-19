#rename multiple files

import os

#rename("old_name","new_name") //present in os library , full names with path e.g./files/desktop/image.jpg
#os.listdir(path) //present is os library

path = input("Enter the directory :")
path = path.replace("\\","/")
l = os.listdir(path)
print(l)
for i in range(len(l)):
    new_name = path+"/image"+str(i)+".jpg" #.jpg is the extension. image file saved as file
    os.rename(path+"/"+l[i],new_name)
k = os.listdir(path)
print(k)

"""
at the ending of path :
all three will work:
images
images\
images/
"""

    

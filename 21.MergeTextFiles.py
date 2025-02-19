import os
import os.path as p
#merge multiple text file into one
files=[]
num = int(input("Enter the number of files:"))
for i in range(num):
    f_name = input("Enter the file name: ")
    files.append(f_name)

merged_data = ""
for i in files:
    name = "files/"+i+".txt"
    if p.isfile(name):
        with open(name,mode="r") as f:
            merged_data = merged_data+f.read()+"\n"
    else:
        print("skipped "+name+" because it doesn't exist")

print(merged_data)
nf = input("Enter the new file name:")
with open("files/"+nf+".txt",mode="x") as f:
    if f:
        print(f.name,"created")
    f.writelines(merged_data)

with open("files/"+nf+".txt",mode="r") as f:
    data = f.read()
    print(data)
    f.seek(0)
    data = f.readlines()
    print(data)


    
    

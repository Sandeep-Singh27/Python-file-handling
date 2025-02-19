#writelines()
"""
used to write group of lines of strings.
group of lines stored in list,tuple or set.
"""
#Syntax
"""
f.writelines(list/set/tuple or string)
"""
f = open("files/3rd video.txt","w")
if f:
    print(f.name,"opened")
    lines_list=["Sandeep","Vimlesh","Tushar","Rayyan"]
    f.writelines(lines_list) #this will overwrite file with "SandeepVimleshTusharRayyan"
    f.writelines("\n")
    for i in range(len(lines_list)):
        lines_list[i] = lines_list[i]+"\n"
    f.writelines(lines_list) #this will overwrite file with "Sandeep\nVimlesh\nTushar\nRayyan\n"
f.close()

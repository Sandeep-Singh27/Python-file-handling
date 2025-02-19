
#Need of file handling-
"""
input --> program -->output

output window is terminal , shell or console .
"""

age = int(input("Enter you age = "))
if age>18:
    print("eligible for voting")
    
#After closing the code
"""
after closing the program , user input can't be used .
user input stored in ram . but we want to work on verasatile application.

so we want to store the data

ways to store data-
1.File handling
2.Database
"""
age = input("Enter your age :")
f = open("data.txt","w")
f.write(age)
f.close()

#again opening after closing
f = open("data.txt","r")
print(f.read())
f.close()

#database vs file handling
"""
1.File redunancy
2.File inconsistency
3.Security problems
"""
#Use of file handling
"""
1.using to handle json files.
2. used in small files.
"""

#reading csv file
import csv #pandas can also be used

#There are two ways in csv module for reading csv
"""*************************************************************************************************"""
#as List
with open("files/titanic.csv",mode="r") as f:
    if f:
        print(f.name,"opened")

    #we cannot use read() directly like how we did for textfile , we have to use reader() from csv
    #variable_name=csv.reader(f,delimiter=",")

    titanic_csv = csv.reader(f,delimiter=",")
    print(titanic_csv)

    for i in titanic_csv:
        print(i)
"""***************************************************************************************************"""
#as Dictionary
with open("files/titanic.csv",mode="r") as f:
    if f:
        print(f.name,"opened")

    #we cannot use read() directly like how we did for textfile , we have to use reader() from csv
    #variable_name=csv.reader(f,delimiter=",")

    titanic_csv = csv.DictReader(f,delimiter=",")
    print(titanic_csv)

    for i in titanic_csv:
        print(i)
        

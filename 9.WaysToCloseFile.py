#ways of closing files:-
"""
close() //python doesn't guarantee that file will be closed using close() definitly
"""

#normal way
"""
f = open(file_name)
Operations on file
f.close()

if there is an exception during operations it will break the flow of code and file might not get closed
"""

#Exception Handling
"""
try:
    f = open(filename)
    #operations on file
    
finally:              //finally block always gets executed either there is a exception or not
    f.close
"""
#using "with" statement // no need to explicitly close file , python will automatically close in anycase.
"""
with open("filename") as f:
    #operations
"""
#example of with
"""
with open("filename") as f:
    data=f.read()
    print(data)
"""



#closing a file
"""
After performining operations we have to close the file
close()
"""
#Syntax
"""
file_handler.close()   //f.close()
"""
#What happens when we close the file
"""
file_handler object gets deleted from the memory

now it is not accessible anymore unless we open() the file again
"""

#if we don't close the file
"""
after program execution , python garbage collector will destroy file object and closes it automatically.
"""
#note - python garbage collector program only works after execution of whole code
"""
the might get corrupt or get unexpected changes , for that reason closing a file is a good practice.
memory wastage if not close
"""


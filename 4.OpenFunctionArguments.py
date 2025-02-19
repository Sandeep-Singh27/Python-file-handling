#open function arguements
"""
f = open(filename, mode="r", buffering, encoding = None, errors = None, newline=None, closefd=True)
"""
#buffering
"""
It is an integer value
It is used to set buffer size of file

buffer_memory = stores data that is going to be processed , part of Main memory.

Suppose
*************************************************************
1GB data    Main memory      My python program
           (buffer memory)
divides data into n of chunks

*************************************************************
always Positive integer
in text mode buffer size should be 1 or more than 1.
in binary mode buffer size can be 0
default size = 4096 to 8192 bytes
"""
#encoding
"""
used to decode and encode file
should be used only in text mode only
default value depends on Operating System
for windows :- cp1252 , UTF8
"""
#errors
"""
Represents how encoding and decoding errors are to be handled
Cannot be used in binary mode
Some standard values are :- strict,ignore,replace etc
"""
#newline = \n , \r , \r\n.
"""
can vary according to file
so let it be as default
"""



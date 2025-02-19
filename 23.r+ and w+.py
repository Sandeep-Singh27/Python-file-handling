#r+ and w+ mode file handling
"""
r will only allow to read
w will only allow to write
"""
#that's why
"""
we use r+ and w+
"""
#r+ mode // read and then write(append)
"""
Read and Write mode .
cursor at the beginning of file.
When want to read data first and then write(append).

throws error if file doesn't exist
opens file without truncating (file used to get empty . after that you used to overwrite it)
"""
#w+ mode // write then read
"""
cursor at beginning
creates new file if file doesn't exist
opens file with truncate(erasing all data to overwrite it again)
"""

#Mode of Opening File:-
"""
Types of mode :-
1.Text Modes
2.Binary Modes
"""
#Text Mode
"""

"r" mode is a text mode
python treats content as "str"

decoding and encoding gets performed when we use text mode

"""
#Binary mode
"""
Opens directly without decoding or encoding.

Content gets treated as a "bytes"

e.g. images , audio , videos
"""
#text mode list
"""
r : Open file for reading only . if file doesn't exist , it will show "FileNotFoundError".(default)
w : Open file for writing only. if the file doesn't exist , it will create a file.

a : Open for appending. it appends new data at the end of file. if file does not exist , it creates a new file.

x : open for exclusive creation for writing. The specified file must not be available.
    It creates a new file and then we write data into it.if file exists , it will give an error.

r+ : open for reading and then writing.
w+ : Open for writing and then reading.
a+ : Open for appending and then reading.
"""

#Binary Modes list
"""
rb : Open for reading in binary mode.
wb : Open for writing in binary mode.
ab : Open for appending.
xb : Open for exclusive creation and writing,
rb+ : Open for read and then write in binary.
wb+ : Open for writing and then reading in binary.
ab+ : Open for append and then read in binary.
"""
#Binary vs text
"""
Text

Hi
world

Binary

Hi\nBinary
"""


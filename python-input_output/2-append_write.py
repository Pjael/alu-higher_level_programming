#!/usr/bin/python3
"""defines function that appends string at end of text file"""

def append_write(filename="", text=""):
    """appends string to text file"""
    with open(filename, 'a') as f:
        return f.write(text)

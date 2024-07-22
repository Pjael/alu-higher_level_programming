#!/usr/bin/python3
"""defines function to read text file   and print it in stdout"""

def read_file(filename=""):
    """reads text and print in stdout"""
    with open(filename) as f:
        print(f.read(), end='')

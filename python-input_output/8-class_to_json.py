#!/usr/bin/python3
"""defines function to return dictioannry description with data\ structure for JSON serialization of an object"""

def class_to_json(obj):
    """returns dictionnary description for JSON serialization"""
    return obj.__dict__

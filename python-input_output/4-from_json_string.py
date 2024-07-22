#!/usr/bin/python3
"""defines functionthat returns an object represented by JSON string"""

def from_json_string(my_str):
    """returns object from JSON"""
    import json
    return json.loads(my_str)

#!/usr/bin/python3
"""defines function that returns JSON representation of object"""

def to_json_string(my_obj):
    """retunrs JSON representation of an object"""
    import json
    return json.dumps(my_obj, ensure_ascii=False)

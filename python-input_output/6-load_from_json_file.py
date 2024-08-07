#!/usr/bin/python3
"""defines function to create an object from a JSON file"""

def load_from_json_file(filename):
    """creates object form JSON representation in file"""
    import json
    with open(filename, 'r') as f:
        return json.load(f)

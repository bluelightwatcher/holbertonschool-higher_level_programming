#!/usr/bin/python3
"""Module adds all arguments to a Python list, and then save them to a file."""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


filename = "add_item.json"

"""Step 1: Try to load the existing list from the JSON file"""
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = [] 

""" Step 2: Add new arguments passed from the command line to the list"""
items.extend(sys.argv[1:])

""" Step 3: Save the updated list back to the file in JSON format """
save_to_json_file(items, filename)
